# 1. 다익스트라 힙큐로 풀이
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 초기화
n,m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b) # 도착지(b)까지의 거리는 다 1
  graph[b].append(a) # 반대도 저장

x,k = map(int, input().split())

# start에서 end까지, pass_node를 안거치고 가는 최단 경로 찾기
def check(start, end, pass_node):
  # 시작 노드 초기화
  distance = [INF] *(n+1)
  distance[start] = 0
  q = []
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q) #힙큐는 처음에 거리로 오름차순 정렬
    if now == pass_node:
      continue
    if distance[now] < dist:
      continue
    for i in graph[now]:
    # i는 도착장소, 거리는 1로 고정
      cost = dist + 1
      if cost < distance[i]:
        distance[i] = cost
        heapq.heappush(q, (cost, i))

  if distance[end] == INF:
    return -1
  else:
    return distance[end]

dist_first = check(1, k, x)
dist_sec = check(k, x, 1)

if dist_first == -1 or dist_sec == -1:
  print(-1)
else:
  result = dist_first + dist_sec
  print(result)

  
  
# 2. 플로이드
  
INF = int(1e9)
n,m = map(int, input().split())
# 최초는 무한으로 초기화
graph = [[INF] * (n+1) for i in range(n+1)]

# 자기자신 0으로 초기화
for a in range(n+1):
  for b in range(n+1):
    if a== b:
      graph[a][b] = 0

# 거리 초기화
for i in range(m):
  a,b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

# 최종 장소 x, 거쳐갈 장소 k
x, k = map(int, input().split())

# 플로이드 워셜
for i in range(1, n+1):
  for j in range(1, n+1):
    for k in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 정답 찾기
dist = graph[1][k] + graph[k][x]

if dist == INF:
  print(-1)
else:
  print(dist)
