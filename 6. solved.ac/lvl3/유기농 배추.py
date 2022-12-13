from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def start():
    m, n, k = map(int, input().split())
    graph = [[0] * (n) for _ in range(m)]
    visited = [[False] * (n) for _ in range(m)]
    for i in range(k):
        y, x = map(int, input().split())
        graph[y][x] = 1

    def bfs(sx, sy):
        nonlocal m, n, visited, graph
        q = deque([(sx, sy)])
        while q:
            tx, ty = q.popleft()
            for i in range(4):
                nx = tx + dx[i]
                ny = ty + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if graph[nx][ny] == 1:
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

    answer = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and graph[i][j] == 1:
                visited[i][j] = True
                answer += 1
                bfs(i, j)

    print(answer)


for _ in range(tc):
    start()
