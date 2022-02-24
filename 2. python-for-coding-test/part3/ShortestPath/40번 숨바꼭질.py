# 힙큐 사용안하고 => 힙큐는 간선거리순으로 정렬할 떄 활용
# BFS 사용함! => 이 문제는 간선거리가 어차피 1이니까
from collections import deque

q = deque()
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
  

distance = [-1] * (n+1)
distance[1] = 0

q.append(1)
while q:
  now = q.popleft()
  for i in graph[now]:
    if distance[i] == -1:
      distance[i] = distance[now] + 1
      q.append(i)

max_dist = 0
cnt = 0
for i in range(len(distance)):
  cur_dist = distance[i]
  if max_dist < cur_dist:
    cnt = 1
    num = i
    max_dist = cur_dist
  elif max_dist == cur_dist:
    cnt += 1

print(distance)
print(num, max_dist, cnt, end=' ')
