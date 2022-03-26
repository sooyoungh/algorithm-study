# 1. BFS - 연결된 노드 통해서 최단 거리 찾기
from collections import deque

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
  start, end = map(int, input().split())
  graph[start].append(end)

distance = [-1] * (n+1)
distance[x] =0

queue = deque([x])
while queue:
  now = queue.popleft()
  # 한번도 방문 안했을 때 큐 안에 넣기
  for i in graph[now]:
    if distance[i] == -1:
      distance[i] = distance[now] + 1
      queue.append(i)

for i in range(1, n+1):
  if distance[i] == k:
    print(i)

# 2. 다익스트라
import heapq
n, m, k, x = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = [(0, x)]

while q:
    dist, node = heapq.heappop(q)
    for next in graph[node]:
        if distance[next] == -1:
            heapq.heappush(q, (dist + 1, next))
            distance[next] = dist + 1

print(distance)
