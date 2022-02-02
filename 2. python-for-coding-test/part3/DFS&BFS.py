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

for i in range(1, len(distance)):
  if distance[i] == k:
    print(i)
