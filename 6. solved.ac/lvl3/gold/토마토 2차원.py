from collections import deque
import sys
input = sys.stdin.readline

q = deque()

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

flag = True
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer = 0
            flag = False
            break
        else:
            answer = max(answer, graph[i][j])
    if not flag:
        break

print(answer-1)
