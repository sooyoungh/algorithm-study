INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]* (n+1) for i in range(n+1)]

# 초기화 - 자기자신으로 가는 거리를 0으로
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

# 초기화 - 거리 나타내는 그래프이자 답
for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a][b] = c

# 점화식 - 최단 거리 찾기
for k in range(1, n+1):
  for a in range(1,n+1):
    for b in range(1, n+1):
      graph[a][b] = min( graph[a][b], graph[a][k] + graph[k][b] )
