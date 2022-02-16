from collections import deque

v,e = map(int, input().split())
indegree = [0] *(v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
  a,b = map(int, input().split())
  graph[a].append(b)
  # b에 도착하는 경우의 수 (진입차수 구하기!)
  indegree[b] += 1

def topology_sort():
  result = []
  q = deque()

  # 최초 시작 노드 찾기
  for i in range(1, v+1):
    if  indegree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()   # v번 만큼
    result.append(now)
    for i in graph[now]:  # 전부 다 합하면 총 e만큼
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
    
    
  for i in result:
    print(i, end = ' ')
      
topology_sort()
