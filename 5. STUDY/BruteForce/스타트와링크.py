# 1. 조합
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
data = list(combinations(range(n), n//2))

result = 1e9

for case in data:
    start, link = 0, 0
    for i, j in combinations(case, 2):
        start += (graph[i][j] + graph[j][i])

    tmp = list(set(range(n)) - set(case))
    for i, j in combinations(tmp, 2):
        link += (graph[i][j] + graph[j][i])

    result = min(result, abs(start-link))

print(result)


# 2. dfs
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
start_arr = []
result = 1e9


def dfs(depth, idx):
    global result

    if depth == n//2:  # 이때 최종 연산하기!
        start, link = 0, 0
        link_arr = list(set(range(n)) - set(start_arr))
        for i in range(0, n // 2 - 1):
            for j in range(i+1, n // 2):
                x, y = start_arr[i], start_arr[j]
                a, b = link_arr[i], link_arr[j]
                start += graph[x][y] + graph[y][x]
                link += graph[a][b] + graph[b][a]

        result = min(result, abs(start-link))
        return

    for i in range(idx, n):
        if not i in start_arr:
            start_arr.append(i)
            dfs(depth+1, i+1)
            start_arr.pop()


dfs(0, 0)
print(result)
