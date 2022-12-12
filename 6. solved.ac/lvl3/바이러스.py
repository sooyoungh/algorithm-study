# 1) BFS
# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# link = int(input())
# graph = [[] for _ in range(n+1)]
# for _ in range(link):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# visited = []
# q = deque()
# q.append(1)
# while q:
#     now = q.popleft()
#     if now in visited:
#         continue
#     visited.append(now)

#     for next in graph[now]:
#         if not next in visited:
#             q.append(next)

# print(len(visited) - 1)

# 2) DFS
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
link = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(link):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)


def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    for next in graph[x]:
        if not visited[next]:
            dfs(next)


dfs(1)
answer = 0
for i in range(1, n+1):
    if visited[i]:
        answer += 1
print(answer-1)
