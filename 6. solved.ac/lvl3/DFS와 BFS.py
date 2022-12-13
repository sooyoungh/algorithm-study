from collections import deque
import sys
input = sys.stdin.readline

n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i] = sorted(graph[i])


def get_bfs(start):
    visited = [False] * (n+1)
    q = deque([start])
    visited[start] = True
    answer = [start]

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                answer.append(next)
                q.append(next)
                visited[next] = True
    return answer


def get_dfs(start):
    visited = [False] * (n+1)
    visited[start] = True
    answer = [start]

    def dfs(x):
        nonlocal visited
        visited[x] = True

        for next in graph[x]:
            if not visited[next]:
                answer.append(next)
                dfs(next)

    dfs(start)
    return answer


def print_result(result):
    for i in result:
        print(i, end=' ')


print_result(get_dfs(start))
print()
print_result(get_bfs(start))
