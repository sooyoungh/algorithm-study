import copy
wall = []
n, m = 5, 6
fire = [[4, 3], [5, 4], [2, 5], [3, 2]]

max_result = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 0. new_graph 셋팅하기 - 불의 위치 // 벽의 위치는 따로!! => 합쳐야 될거같음!
new_graph = [[False] * (m+1) for _ in range(n+1)]
for x, y in fire:
    new_graph[x][y] = True


# 2. 퍼뜨리기 - DFS 혹은 BFS
def dfs(x, y, time, tmp):
    if checkClear():
        return time
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tmp[nx][ny] == False:
                tmp[nx][ny] = True
            if wall[nx][ny] != '#':
                dfs(nx, ny, time+1, tmp)


# 3. 인화물질 있는 지 검사하기
# => 인화물질은 따로 배열에 넣기
def checkClear():
    for x, y in fire:
        if graph[x][y] == -1:
            return False
    return True


# 1. 모든 곳에서 시작하기
for i in range(n):
    for j in range(m):
        if wall[i][j] != '#':
            tmp = copy.deepcopy(new_graph)
            max_result = max(dfs(i, j, 0, tmp), max_result)
