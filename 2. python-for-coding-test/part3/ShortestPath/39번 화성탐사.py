# 1. 내 풀이
# 힙큐 사용안함
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
        print((nx,ny), result[nx][ny], end=' ')
        q.append((nx,ny))
        print()
      
      
print(result)
