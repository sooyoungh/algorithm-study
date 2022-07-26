n = int(input())
graph = []
for i in range(n):
    # 아래 map 사용시
    # input()은 0110100, // input().split()은 0 1 1 0 1 0 0인 경우
    data = list(map(int, input()))
    graph.append(data)
visited = [[-1] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, visited, group):
    visited[x][y] = group
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if (graph[nx][ny]):
                if (visited[nx][ny] == -1):
                    dfs(nx, ny, visited, group)


group = -1  # 후에 배열 인덱스로 사용할 예정
for i in range(n):
    for j in range(n):
        # 새 그룹을 만들수 있는가
        if graph[i][j]:
            if (visited[i][j] == -1):
                group += 1
                dfs(i, j, visited, group)

print(group+1)  # 0부터 시작했으니 갯수는 +1 해주어야 함

arr = [0] * (group+1)
for i in range(n):
    for j in range(n):
        if visited[i][j] != -1:
            group_n = visited[i][j]
            arr[group_n] += 1

arr.sort()
for k in range(group+1):
    print(arr[k])
