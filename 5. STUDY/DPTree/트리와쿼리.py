# dp로 각 노드의 자식들 수 저장해놓기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(start):
    dp[start] = 1
    for i in graph[start]:
        if not dp[i]:  # 방문안했던 자식이면 dfs() 먼저
            dfs(i)
            dp[start] += dp[i]


n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
dp = [0] * (n+1)

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


# 시작은 전체 트리의 루트에서
# (연산은 말단 노드부터)
dfs(r)

for _ in range(q):
    root = int(input())
    print(dp[root])
