import copy
import sys
sys.setrecursionlimit(100000)
s = sys.stdin.readline  # 기존 input() 대신 s() 사용하기

n = int(s())
graph = []

for i in range(n):
    data = list(map(int, s().split()))
    graph.append(data)

max_height = max(map(max, graph))  # 2차원 배열 최댓값
min_height = min(map(min, graph))  # 2차원 배열 최소값


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, h, tmp):
    tmp[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > h:
                if not tmp[nx][ny]:
                    dfs(nx, ny, h, tmp)


result = []
visited = [[False] * n for _ in range(n)]

for h in range(min_height, max_height):
    tmp = copy.deepcopy(visited)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h:  # h이하면 잠기니까, h초과인 애들의 그룹 만들기!
                if not tmp[i][j]:
                    cnt += 1
                    dfs(i, j, h, tmp)  # 한 그룹 만들기 시작!
    result.append(cnt)

print(max(result))
