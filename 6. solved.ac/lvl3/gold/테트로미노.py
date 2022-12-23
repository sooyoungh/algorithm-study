import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
max_result = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# ㅏ 모양 빼고는 4번의 상하좌우 이동으로 만들수 있음


def dfs(x, y, tmp, cnt):
    global max_result
    if cnt == 4:
        max_result = max(max_result, tmp)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, tmp + graph[nx][ny], cnt + 1)
                visited[nx][ny] = False


def special_shape(x, y):
    global max_result

    for i in range(4):  # ㅏ,ㅓ,ㅗ,ㅜ 4가지 방향!
        tmp = graph[x][y]
        for j in range(3):
            k = (i+j) % 4
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                tmp += graph[nx][ny]
            else:
                break
        max_result = max(max_result, tmp)


for i in range(n):
    for j in range(m):
        # dfs
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = False

        # ㅏ 모양
        special_shape(i, j)

print(max_result)
