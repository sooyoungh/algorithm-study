from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = []


def bfs(i, j):
    cnt = 1
    q = deque()
    q.append([i, j])
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    cnt += 1

    return cnt


for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            answer.append(bfs(i, j))

answer.sort()

group_n = len(answer)
print(group_n)
for i in range(group_n):
    print(answer[i])
