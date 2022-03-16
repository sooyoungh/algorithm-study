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
 
def bfs():
  testgraph = copy.deepcopy(graph)
  q = deque(virus)
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
          if testgraph[nx][ny] == 0:
            testgraph[nx][ny] = 2
            q.append((nx, ny))
 
  count = 0
  for i in range(N):
    for j in range(M):
      if testgraph[i][j] == 0:
        count += 1
  
  return count
 
 
answer = 0
for data in combinations(blank, 3):
  for x, y in data:
    graph[x][y] = 1
  answer = max(answer, bfs()) # 이떄, 벽만 설치하고, 내부에서 바이러스 퍼지는건 원본 복사 후 진행!
  for x, y in data:
    graph[x][y] = 0
 
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

# 시작 부분 함수로 나눠서 
def dfs_start(tmp):
  global result
  for i in range(n):
    for j in range(m):
      if tmp[i][j] == 2:
        dfs_spread(i,j, tmp)
  result = max(result, get_score(tmp))
  return

for case in combinations(empty, 3):
  tmp = copy.deepcopy(data)
  for i in case:
    tmp[i[0]][i[1]] = 1
  dfs_start(tmp)
  
print(result)
  
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
  

# 틀린 풀이 (시작단계)
# 원본 데이터를 바꾸면 오류 발생함 (중간에 바뀌어서,,) => deepcopy 사용해야함
# 아래는 틀린 풀이! 원본을 따로 복사 해줘야함
for case in combinations(empty, 3):
  for x,y in case:
    data[x][y] = 1
  dfs_start(data)  ==> 여기서 원본 데이터도 변경(바이러스)되니까, 이 문제에서는 원본을 따로 복사하여 탐색해야함
                        반면 20번 감시 피하기 문제에서는 process()에서 원본을 바꾸지 않으니까 가능함
                      혹은 여기서도 중간에 복사해서 원본 데이터를 바꾸지 않으면 가능!
  for x,y in case:
    data[x][y] = 0
  




# 이코테- 시간초과-------------------------------------------------------- (DFS 2번 사용)
n,m = map(int, inp7ut().split())
data = []
temp = [[0]*m  for i in range(n)]

for _ in range(n):
  data.append(list(map(int, input().split())))
  
result = 0

# 재귀적으로 바이러스 퍼뜨리기!
def virus(x,y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and ny >=0 and nx < n and ny < m:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        virus(nx,ny)

# 0인 안전지역 카운트
def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[n][m] == 0:
        score += 1
  return score

def dfs(count):
  global result
  # 울타리가 3개 설치 된 경우
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j] #어차피 매번 바뀌니까 temp를 매번 0으로 초기화시킬 필요없음!!
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i,j)
    result = max(result, get_score())
    return 
  # 울타리 갯수 모자를 경우
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        data[i][j] = 0
        count -= 1
        
dfs(0)
print(result)
        
