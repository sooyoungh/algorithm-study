from itertools import combinations
n = int(input())
graph = []
teachers = []
spaces = []

for i in range(n):
  graph.append(list(input().split()))
  for j in range(n):
    if graph[i][j] == 'T':
      teachers.append((i,j))
    if graph[i][j] == 'X':
      spaces.append((i,j))

def watch(x,y, direction):
  if direction == 0:
    while y >= 0:
      if graph[x][y] == 'S':
        return False
      if graph[x][y] == 'O':
        return True
      y -= 1
  if direction == 1:
    while y < n:
      if graph[x][y] == 'S':
        return False
      if graph[x][y] == 'O':
        return True
      y += 1
  if direction == 2:
    while x >= 0:
      if graph[x][y] == 'S':
        return False
      if graph[x][y] == 'O':
        return True
      x -= 1
  if direction == 3:
    while x < n:
      if graph[x][y] == 'S':
        return False
      if graph[x][y] == 'O':
        return True
      x += 1
  return True

# 한명이라도 감지되면 
def process():
  for x,y in teachers:
    for i in range(4):
      if not watch(x,y,i):
        return False
  return True

find = False
for case in combinations(spaces, 3):
  for x,y in case:
    graph[x][y] = 'O'
  if process(): # 이 조합에서 학생 다 안보이는 경우 (정답이 되는 조합!)
    find = True
    break
  for x,y in case:
    graph[x][y] = 'X'

if find:
  print("YES")
else:
  print("NO")
