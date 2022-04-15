n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left(d):
    d = (d-1) % 4
    return d


count = 1
visited[x][y] = 1

while 1:
    flag = False
    for i in range(4):
        d = turn_left(d)
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    x, y = nx, ny
                    count += 1
                    flag = True
                    break

    if not flag:
        # 후진하나 방향은 유지 되어야하므로 d값은 건드리지 말것
        nx = x - dx[d]
        ny = y - dy[d]

        #d = (d+2) % 4
        #nx = x + dx[d]
        #ny = y + dy[d]

        if graph[nx][ny] != 1:
            x = nx
            y = ny
        else:
            print(count)
            break
