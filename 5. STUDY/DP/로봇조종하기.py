# //// 수정중
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# z
# 1 : 오른
# 2 : 왼
# 3 : 아래

dx = [0, 0, 1]
dy = [1, -1, 0]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 이전 방향이 z일때의 (x,y)의 최댓값 저장하는 3차원 배열
MIN = -1e9
dp = [[[MIN] * 3 for _ in range(n)] for _ in range(m)]

# 첫줄
for j in range(m):
    for k in range(3):
        dp[0][]


def dfs(x, y, z):  # 이전에 z 방향이었을때 (x,y)의 최댓값
    if x == n-1 and y == m-1:
        return graph[x][y]

    if dp[x][y][z] != -1:
        return [x][y][z]

    dp[x][y][z] = -1e9

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if z == 1 and (dx, dy) == (0, -1):
            continue
        if z == 2 and (dx, dy) == (0, 1):
            continue

        if 0 <= nx < n and 0 <= ny < m:
            dp[x][y][z] = max(dp[x][y][z], dfs(x, y, z) + graph[x][y])
    return dp[x][y][z]


print(dfs(0, 0, -1))
