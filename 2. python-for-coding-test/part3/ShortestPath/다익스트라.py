import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

# a에서 b까지 가는 경로 길이는 c
for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))
# ---------- 여기까지 초기화 완료

# 방문 안한 노드 중에서 최단 거리가 가장 짧은 노드
def get_smallext_node():
  min_value = INF
  index = 0
  for i in range(n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  # 시작노드 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
   # 시작 노드 제외 초기화 -> 이 노드를 거쳐 가는게 더 짧은 지 판단하여 업데이트
  for i in range(n-1):
    # 가장 작은 노드를 찾기 위해서  O(n)
    now = get_smallext_node()
    visited[now] = True
    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost <distance[j[0]]: # 거쳐서 갈 때가 더 짧을 경우
        distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("infitity")
  else:
    print(distance[i])
        
  
