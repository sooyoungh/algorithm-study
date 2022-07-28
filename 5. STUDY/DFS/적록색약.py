import sys
sys.setrecursionlimit(100000)
s = sys.stdin.readline
n = int(s())
graph = []
for _ in range(n):
    data = list(s())
    graph.append(data)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, color, tmp):
    tmp[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not tmp[nx][ny]:
                if graph[nx][ny] == color:
                    dfs(nx, ny, color, tmp)


def dfs_red_green(x, y, tmp):
    tmp[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not tmp[nx][ny]:
                if graph[nx][ny] != "B":
                    dfs_red_green(nx, ny, tmp)


normal = 0
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] == "R":
                normal += 1
                dfs(i, j, "R", visited)
            elif graph[i][j] == "G":
                normal += 1
                dfs(i, j, "G", visited)
            else:
                normal += 1
                dfs(i, j, "B", visited)

red_green = 0
visited2 = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            if graph[i][j] == "B":
                red_green += 1
                dfs(i, j, "B", visited2)
            else:
                red_green += 1
                dfs_red_green(i, j, visited2)


print(normal)
print(red_green)
