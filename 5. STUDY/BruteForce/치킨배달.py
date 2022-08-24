# 조합
from itertools import combinations
import sys
input = sys.stdin.readline

chicken = []
house = []

n, m = map(int, input().split())
graph = []
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))
        elif graph[i][j] == 1:
            house.append((i, j))

result = 1e9

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 각 집마다 치킨거리 찾고,
# 최종 모든 치킨 거리의 합의 최소 구하기!
for case in combinations(chicken, m):  # 치킨집 m개의 조합
    tmp = 0
    for hx, hy in house:  # 집 x,y 좌표 - 각 집마다
        min_len = 1e9
        for x, y in case:  # 치킨집 각각의 x,y좌표
            min_len = min(min_len, abs(hx-x) + abs(hy-y))
        tmp += min_len
    result = min(result, tmp)

print(result)
