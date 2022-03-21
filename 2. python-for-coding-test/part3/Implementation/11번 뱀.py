# 1. 교재 - stack 사용, FIFO
# 자료 구조 : snake(뱀정보-배열/큐), info(방향정보-큐), data(그래프정보-2차원 배열)
n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)]
info = []

for _ in range(k):
  a,b = map(int, input().split())
  data[a][b] = 1

l = int(input())
for _ in range(l):
  x, c = input().split()
  info.append((int(x),c))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, c):
  if c == "L":
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
  return direction

def simulate():
  x,y = 1,1
  data[x][y] = 2
  direction = 0
  time = 0
  index = 0
  # 꼬리가 앞 쪽
  snake = [(x,y)]
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 접근할 수 있는 곳이면
    if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2 :
      if data[nx][ny] == 0:
        data[nx][ny] = 2
        snake.append((nx,ny))
        px, py = snake.pop(0)
        data[px][py] = 0
      if data[nx][ny] == 1 :
        data[nx][ny] = 2
        snake.append((nx,ny))
    # 접근 불가
    else:
      time += 1
      break
    
    # 여기부터는 다음 시간 체크
    time += 1
    x,y = nx, ny
    if index < l and time == info[index][0]:
      direction = turn(direction, info[index][1])
      index += 1
  return time

print(simulate())
