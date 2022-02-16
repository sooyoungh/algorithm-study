import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)] # 행의 개수만!
distance = [INF] * (n+1)

for _ in range(m):
  a,b,c = map(int, input().split())
  # a에서 출발해서 b에 도착할때 거리가 c
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue
      
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[now]:
        distance[i[0]] = cost
        # 짧은 거리 해당되면 힙큐에 넣기 -> 얘를 통해서 또 최단거리가 나오는 지 체크용
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)
