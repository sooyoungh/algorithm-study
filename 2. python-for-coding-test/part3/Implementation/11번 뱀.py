from collections import deque
import copy
n = int(input())
graph = [[0]*(n+1) for i in range(n+1)]
apple = int(input())
for i in range(apple):
  x,y = map(int, input().split())
  graph[x][y] = 2

direct = int(input())
direct_list = deque([])

for i in range(direct):
  sec, d = input().split()
  direct_list.append((int(sec), d))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

cnt = 0
graph[1][1] = 1
x,y = 1,1
direct_num = 0
sec, d = direct_list.popleft()

snake = []
snake.append((x,y))

def restart(snake, x,y):
  arr = []
  arr.append((x,y))
  for i in range(len(snake)):
    arr.append(snake[i])
  return arr

while True:
  if cnt == sec:
    if d =='L':
      direct_num  = (direct_num-1) % 4
    elif d =='D':
      direct_num  = (direct_num+1) % 4
    if len(direct_list) > 0:
      sec, d = direct_list.popleft()
    
  nx= x + dx[direct_num]
  ny= y + dy[direct_num]

  if nx <= 0 or nx > n or ny <= 0 or ny > n:
    cnt += 1
    print(1)
    
    break
  new = graph[nx][ny]
  if new == 1:
    cnt += 1
    print(nx,ny)
    break
  elif new == 2:
    graph[nx][ny] = 1
    snake = copy.deepcopy(restart(snake, nx,ny))
    
  elif new == 0:
    graph[nx][ny] = 1
    tail_x,tail_y = snake.pop()
    graph[tail_x][tail_y] = 0
    # 새 노드 넣어주기
    snake = copy.deepcopy(restart(snake, nx,ny))
    
  x,y = nx, ny
  cnt += 1
  print(x,y, cnt)
  print('snake : ', snake)

print(cnt)
