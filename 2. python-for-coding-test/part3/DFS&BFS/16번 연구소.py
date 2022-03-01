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
        
