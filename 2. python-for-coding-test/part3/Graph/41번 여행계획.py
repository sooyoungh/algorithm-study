# 경로가 있기만 하면 OK니까
# 플로이드에서 max 시용!!
from collections import deque
n,m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))
  
data = list(map(int, input().split()))
q = deque()

for i in range(n):
  for j in range(n):
    for k in range(n):
      graph[i][j] = max(graph[i][j], graph[i][k]+graph[k][j])

for i in range(len(data)):
  q.append(data[i])

flag = "YES"
before = q.popleft()
while q:
  now = q.popleft()
  if graph[before][now] == 0:
    flag = "NO"
    break
  before = now

print(flag)
