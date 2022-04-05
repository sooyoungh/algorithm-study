# 1. 2차원 그래프를 BFS로  -> 시간초과
from itertools import combinations
from collections import deque
import copy
n, m = map(int, input().split())
graph = []
chick = []
house = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 2:
            chick.append((i, j))
            graph[i][j] == 0
        if graph[i][j] == 1:
            house.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# house마다의 최단 거리 구하기
def calc(tmp_graph, now_x, now_y):
    dist = [[-1] * n for _ in range(n)]
    q = deque([])
    q.append((now_x, now_y)) # 왜 처음부터 초기화하면 오류??
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                    if tmp_graph[nx][ny] == 2:
                        return dist[nx][ny]


result = 1e9
for case in combinations(chick, m):
    new_result = 0
    tmp = copy.deepcopy(graph)
    for x, y in case:
        tmp[x][y] = 2
    for i, j in house:
        new_result += calc(tmp, i, j)
    result = min(result, new_result)

print(result)

# 2. 각 집마다 각각의 치킨집의 거리 구하기 (2차원 배열X)
# 이 문제는 연결성을 고려할 필요가 없기 때문에 BFS로 할 필요X
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반 집
        elif data[c] == 2:
            chicken.append((r, c)) # 치킨집

# m개의 치킨 집 경우의 수
candidates = list(combinations(chicken, m))

# 치킨 거리의 합 구하기
def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

# 치킨 거리의 합의 최소 찾기
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
