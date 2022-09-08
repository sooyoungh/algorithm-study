# 시작 위치랑 가장 오래 이동한 일수 구하기
# DP + DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dxdy = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(x, y):
    # 1) 한번도 방문한 적 없는 노드라면
    if dp[x][y] == 0:
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > graph[x][y]:
                    # 이동할 수 있으면 dp에 값 업데이트
                    # 4가지 방향 중 최대로 저장!
                    dp[x][y] = max(dp[x][y], dfs(nx, ny))
    # 2) 이미 한번 방문한 적있으면 dp != 0
    # -> 그때의 기록에 +1만 해주기

    # 한번 이동한 거니까 +1
    return dp[x][y] + 1


answer = 0
# 매 시작 노드들마다 DFS
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)
