# 힙큐나 그냥 큐 사용하고 q.sort()
import heapq
q = []
n, k = map(int, input().split())
graph = []
for i in range(n):
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
  # 현재 정보 큐에 넣기
  for i in range(n):
    for j in range(n):
      heapq.heappush(q,(graph[i][j], i,j) )
  while q:
    target, i, j = heapq.heappop(q)
    spread(graph, i, j)

print(graph[x-1][y-1])
print(graph)


# 2. 힙큐 + BFS
import heapq
n, k = map(int, input().split())
graph = []
virus = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            heapq.heappush(virus, (graph[i][j], (i, j)))

s, x, y = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def spread(virus):
    global graph
    new_virus = []
    while virus:
        num, (now_x, now_y) = heapq.heappop(virus)
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = num
                    heapq.heappush(new_virus, (num, (nx, ny)))
    return new_virus


for i in range(s):
    virus = spread(virus)

print(graph[x-1][y-1])
