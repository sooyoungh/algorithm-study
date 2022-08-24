# algorithm-study

[5. STUDY](/5.%20STUDY/study.md)

### 배열 복사하기

- 깊은 복사

```py
 import copy
 result = copy.deepcopy(data)
```

- 얕은 복사 -> 원래 배열도 값이 변경

```py
result = data
# 혹은
result = data.copy()
# 혹은
result = list(data)
```

- 리스트 슬라이싱 [:]

```py
# 1차원에서는 깊은 복사, 2차원에서는 얕은 복사
result = data[:]

# 2차원에서 깊은 복사 원하면
result = [item[:] for item in data]

```

[배열 복사하기 - 깊은 복사, 얕은 복사](https://blockdmask.tistory.com/576)

- 입력받기

```python
input().split() => 문자열
```

- 2차원 배열 초기화

```python
# 줄로 들어올 경우, 행의 갯수만 알면 OK
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

# 행 초기화, 열 갯수는 다 다를수도 있음
graph  = [[] for i in range(n)]

# 행, 열 다 초기화 + 선언하고 싶을 때
graph = [ [0]*m for i in range(m)]
```

- 문자와 숫자 변환

```python
ord()
int()
```

### 구현

- 상하좌우 → dx,dy 따로 / 튜플로 한번에

```python
n = int(input())
x,y = 1,1
plans = input().split() # 문자열 리스트

# L R U D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or nx > n or ny < 1 or ny > n:
    continue
  x,y = nx, ny

print(x,y)
```

```python
steps = [(-2,-1), (1,2)] # 등등
result = 0
x,y = 1,1 # 시작 노드
n = 10 # 한계

for step in steps:
  nx = x + step[0]
  ny = y + step[1]
  if nx < 1 or nx > n or ny < 1 or ny > n:
    result += 1
```

### DFS BFS

- 큐, 재귀

```python
# stack
stack = []
stack.append(1)
stack.pop()

# deque
from collections import deque

q = deque()
q.append(1)
q.popleft()

q.reverse()
#리스트로 변경
list(q)
```

인접 리스트은 메모리를 덜 쓰나, 속도가 빠르다
인접 행렬은 반대

DFS는 재귀함수로 → 연결 노드들 바로바로 끝까지 탐색
⇒ 하나랑 연결된 노드 하나씩 쭉 끝까지 연결성을 보기 위한

BFS는 큐로 → 주변 노드들 한번에 큐에 넣고 다음 꺼낸거에서 또 주변 노드들 한번에 넣고,,,
⇒ n가지를 한번에 둘러봐야하는 경우

- DFS - 재귀함수로 구현

```python
def dfs(graph, v, visited):
	# 1. 일단 해당 노드는 방문 처리
  visited[v] = True
  print(v, end=' ')
	# 2. 연결된 노드들 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9

dfs(graph, 1, visited)

-----------
n,m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

def dfs(x,y):
  if x <= -1 or x >= n or y <= -1 or y >= n :
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  return False

result = 0
for i in range(m):
  for j in range(n):
    if dfs(i,j) == True:
      result += 1

print(result)
```

- BFS - 큐로 구현

```python
from collections import deque

def bfs(graph, start, visited):
	# 1. 시작 노드 처리
  q = deque()
  visited[start] = True
	# 2. 이후는 계속 큐에 루프
  while q:
    v = q.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)
---------------------
from collections import deque
n,m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  # 최초 시작 노드 설정
  q = deque()
  q.append((x,y))
  while q:
    # q에서 시작할 노드 빼기
    x,y = q.popleft()
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        # 다음에 들어갈 노드 큐에 넣기
        q.append((nx,ny))

  return graph[n-1][m-1]

print(bfs(0,0))
```

### 정렬

- 선택, 삽입, 퀵, 계수, 라이브러리, 람다

### 이진 탐색

- 재귀함수

```python
def binary_search(arr, target, start,end):
	# 재귀는 탈출 조건을 앞에 써줘야 함!
  if start > end:
    return None
  mid = (start + end)//2
  if arr[mid] == target:b
    return mid
  elif arr[mid] > target:
    return binary_search(arr, target, start, mid -1)
  else:
    return binary_search(arr, target, mid + 1, end)

n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n-1)
```

- 반복문

```python
def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start + end)//2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None
```

### 다이나믹

- 피보나치 - 반복, 재귀

```python
# 재귀함수
def fibo(x):
	if x==1 or x ==2:
		return 1
	d[x] = fibo(x-1) + fibo(x-2)
	return d[x]

# 반복문
d[0] = 1
d[1] = 1
for i in range(3, n):
	d[i] = d[i-1] + d[i-2]
```

### 최단 경로

- 다익스트라

: 한 노드(start)에서 모든 노드까지의 최단 거리

```python
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())
graph = [ [] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] *(n+1)

for _ in range(m):
  a,b,cost = map(int, input().split())
  graph[a].append((b,cost)) # (도착지, 거리)

def get_smallest():
  min_value = INF
  index = 0
  for i in range(1,n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  # 시작노드 초기화
  distance[start] = 0
  visited[start] = 0
  for j in graph[start]:
    distance[j[0]] = j[1]

  # 중간 노드가 될 애들은 n-1개니까 (처음 시작 노드 제외!)
  for i in range(n-1):
    now = get_smallest()
    visited[now] = True
    dist = distance[now]
    for j in graph[now]:
      cost = dist + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

# 출력
for i in range(1, n+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])
```

- 다익스트라\_힙큐

: 모든 노드(start)에서 모든 노드까지의 최단 거리 + 갱신되면 힙큐에 넣기

```python
# 최단 경로 - 다익스트라 힙큐
# 중간 노드를 거칠 때마다 더 최단인 경우 갱신
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
  a,b, cost = map(int, input().split())
  graph[a].append((b,cost))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]: # i[0] 도착점, i[1]은 거리
      cost = dist + i[1] #
      if cost < distance[i[1]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)
```

- 플로이드 워셜

: 모든 노드(start)에서 모든 노드까지의 최단 거리 (2차원 배열)

```python
INF = int(1e9)

n = int(input())
m = int(input())
# 기본은 INF으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신은 0
for a in range(1,n+1):
  for b in range(n+1):
    if a==b:
      graph[a][b] = 0

# 초기화
for _ in range(m):
  a,b,cost = map(int, input().split())
  graph[a][b] = cost

# 플로이드 워셜
for i in range(1,n+1):
  for j in range(1,n+1):
    for k in range(1,n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
```

### 그래프

- 서로소, 신장트리

최소 신장 트리를 만드는 데 필요한 최소 비용

```python
def find_parent(parent, x):
	if parent[x] != x:
	parent[x] = find_parent(parent, x)
	return parent[x]

def union_parent(parent, a,b):
	a = find_parent(parent,a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

v,e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
	parent[i] = i

for i in range(e):
	a,b,cost = map(int, input().split())
	edges.append((cost, a,b))

edges.sort()

for edge in edges:
	cost, a,b = edge
	if find_parent(parent,a) != find(parent, b): # 사이클 안만들게 체크
		union_parent(parent, a,b)
		reult += cost

print(result)
```

- 위상 정렬

한 붓 그리기 → 경로 출력,, 커리큘럼

```python
from collections import deque

v,e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
  a,b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1

def topology_sort():
  result = []
  q = deque()
  # 시작 노드 찾기
  for i in range(1,v+1):
    if indegree[i] == 0:
      q.append(i)
  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  for i in result:
    print(i)

topology_sort()
```
