# 1. 내 풀이
# 힙큐 사용안함 -> 속도가 느릴듯??
from  collections import deque

INF = int(1e9)
n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

result = [[INF]* n for i in range(n)]
result[0][0] = graph[0][0]

start = (0,0)
q = deque([start])

dx = [0,0,-1,1]
dy = [-1,1,0,0]

while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x+ dx[i]
      ny = y+ dy[i]
      if nx < 0 or nx>= n or ny < 0 or ny>= n:
        continue
       # nx,ny까지의 경로가 '지금 저장된 경로값 > x,y를 거쳐서 가는 경로값'이면
       # 갱신하고 q에 넣어줌
      if result[x][y] + graph[nx][ny] < result[nx][ny]:
        result[nx][ny] = result[x][y] + graph[nx][ny]
        q.append((nx,ny))
        print((nx,ny), result[nx][ny], end=' ')
        print()
      
print(result)


# 2. 힙큐 사용
import heapq

INF = int(1e9)
n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

distance = [[INF]* n for i in range(n)]

x,y = 0,0
q = [(graph[x][y], x, y)]
distance[x][y] = graph[x][y]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

while q:
  recent_dist, x,y = heapq.heappop(q)
  if distance[x][y] < recent_dist:
    continue
  for i in range(4):
    nx = x+ dx[i]
    ny = y+ dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
      continue
    new_cost = recent_dist + graph[nx][ny]
    if new_cost < distance[nx][ny]:
      distance[nx][ny] = new_cost
      heapq.heappush(q, (new_cost, nx, ny))

print(distance[n-1][n-1])
