# DP + DFS, 트리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
data = [[] for _ in range(n+1)]

for _ in range(n-1):  # N-1개의 줄
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited = [False for _ in range(n+1)]

# dp[i][0] : i가 얼리어답터O, 서브트리에서 얼리어답터의 최소
# dp[i][1] : i가 얼리어답터X, 서브트리에서 얼리어답터의 최소
dp = [[0, 0] for _ in range(n+1)]


def dfs(x):
    # 첫 방문일테니 (dfs 입장 조건)
    visited[x] = True
    dp[x][1] = 1  # 자기사진이 얼리어답터이므로 +1하고 시작

    if not len(data[x]):
        dp[x][0] = 0
        dp[x][1] = 1
    else:
        for i in data[x]:
            if not visited[i]:
                dfs(i)
                # x가 얼리어답터가 아니므로, 자식들은 모두 얼리어답터여야 함!
                dp[x][0] += dp[i][1]
                # x가 얼리어답터이므로, 자식들은 상관없음 -> 그냥 최소인걸로
                dp[x][1] += min(dp[i][0], dp[i][1])


dfs(1)
print(min(dp[1][0], dp[1][1]))
