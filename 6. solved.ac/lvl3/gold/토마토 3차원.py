from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))

diff = [[0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0], ]

while q:
    now_h, now_x, now_y = q.popleft()
    for i in range(len(diff)):
        nh = now_h + diff[i][0]
        nx = now_x + diff[i][1]
        ny = now_y + diff[i][2]
        if 0 <= nh < h and 0 <= nx < n and 0 <= ny < m:
            if graph[nh][nx][ny] == 0:
                graph[nh][nx][ny] = graph[now_h][now_x][now_y] + 1
                q.append((nh, nx, ny))

flag = True
answer = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                answer = 0
                flag = False
                break
            else:
                answer = max(answer, graph[k][i][j])
        if not flag:
            break
    if not flag:
        break

print(answer-1)
