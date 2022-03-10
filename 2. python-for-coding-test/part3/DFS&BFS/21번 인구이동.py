from collections import deque
n,l,r = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))
  
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def process(x,y,index):
  united = []
  united.append((x,y))
  q = deque()
  q.append((x,y))
  union[x][y] = index
  sum = graph[x][y]
  cnt = 1
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
        if l <= abs(graph[x][y] -graph[nx][ny]) <= r:
          q.append((nx,ny))
          union[nx][ny] = index
          sum += graph[nx][ny]
          cnt += 1
          united.append((nx,ny))
          
  for i, j in united:
    graph[i][j] = sum//cnt
  return cnt

result = 0
while True: # 날마다 루프 돌리기
  union = [[-1] *n for i in range(n)]
  index = 0
  # 날마다 모든 나라 탐색하기
  for i in range(n):
    for j in range(n):
      if union[i][j] == -1:
        process(i,j, index)
        index += 1
        
  # 마지막 날은 인구 이동 할 필요 없는 나라들이 n*n가지 => 이러면 while문 종료!
  if index == n*n:
    break
  result += 1

print(result)
