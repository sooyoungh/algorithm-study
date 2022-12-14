import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 연결요소 구하기 => 그룹 수 세기

node, edge = map(int, input().split())

graph = [[] for _ in range(node+1)]
for _ in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (node+1)


def dfs(start):
    visited[start] = True
    for next in graph[start]:
        if not visited[next]:
            dfs(next)


result = 0
for i in range(1, node+1):
    if not visited[i]:
        dfs(i)
        result += 1

print(result)
