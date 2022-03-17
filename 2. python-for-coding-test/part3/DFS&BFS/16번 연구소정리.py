# 벽 3개 세울때 조합 사용, 2차원 배열 복사
# 1. BFS + 조합 4초
from itertools import combinations
from collections import deque
import copy
 
N, M = map(int, input().split())
graph = []
blank = []
virus = []
 
for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(M):
    if graph[i][j] == 0:
      blank.append((i, j))
    elif graph[i][j] == 2:
      virus.append((i, j))
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2-1)
def bfs(tmp):
  q = deque(virus)
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
          if tmp[nx][ny] == 0:
            tmp[nx][ny] = 2
            q.append((nx, ny))
 
  count = 0
  for i in range(N):
    for j in range(M):
      if tmp[i][j] == 0:
        count += 1
  return count
 
answer = 0
for data in combinations(blank, 3):
  tmp = copy.deepcopy(graph)  
  for x, y in data:           
    tmp[x][y] = 1
  answer = max(answer, bfs(tmp))
 
print(answer)



# 2. DFS + 조합으로 풀이 6초
import sys
import copy
from itertools import combinations
input = sys.stdin.readline
n,m = map(int, input().split())
data = []

for _ in range(n):
  data.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

result = 0
empty = []
for i in range(n):
  for j in range(m):
    if data[i][j] == 0:
      empty.append((i,j))

def dfs_spread (x,y, tmp):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m:
      if tmp[nx][ny] == 0:
        tmp[nx][ny] = 2
        dfs_spread(nx,ny, tmp)

def get_score(tmp):
  score = 0
  for i in range(n):
    for j in range(m):
      if tmp[i][j] == 0:
        score += 1
  return score

  
# 시작 부분 한번에
for case in combinations(empty, 3):
  tmp = copy.deepcopy(data)
  for i in case:
    tmp[i[0]][i[1]] = 1
  for i in range(n):
    for j in range(m):
      if tmp[i][j] == 2:
        dfs_spread(i,j, tmp)
  result = max(result, get_score(tmp))
  
print(result)
