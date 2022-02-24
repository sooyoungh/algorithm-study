# 힙큐나 그냥 큐 사용하고 q.sort()
import heapq
q = []
n, k = map(int, input().split())
graph = []
for i in range(n):
  # graph[i] = list(map(int, input().split())))
  graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

# x,y는 무조건 배열안에 정상적으로!
def spread(graph, x,y):
  target = graph[x][y]
  if target == 0:
    return
  if x-1 >= 0 and x-1 < n and graph[x-1][y] == 0:
    graph[x-1][y] = target
  if x+1 >= 0 and x+1 < n and graph[x+1][y] == 0:
    graph[x+1][y] = target
  if y-1 >= 0 and y-1 < n and graph[x][y-1] == 0:
    graph[x][y-1] = target
  if y+1 >= 0 and y+1 < n and graph[x][y+1] == 0:
    graph[x][y+1] = target

for _ in range(s):
  for i in range(n):
    for j in range(n):
      heapq.heappush(q,(graph[i][j], i,j) )

while q:
  target, i, j = heapq.heappop(q)
  spread(graph, i, j)

print(graph[x-1][y-1])
print(graph)
