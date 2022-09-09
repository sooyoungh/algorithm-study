import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(start):
    visited[start] = True

    for i in graph[start]:  # 연결노드들중
        if not visited[i]:  # 자식이라면
            dfs(i)
            dp[start][0] += max(dp[i][0], dp[i][1])
            dp[start][1] += dp[i][0]


n = int(input())
data = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, data[i]] for i in range(n+1)]  # 자기자신 마을의 사람수 초기화
visited = [False for _ in range(n+1)]


dfs(1)
print(max(dp[1][0], dp[1][1]))
