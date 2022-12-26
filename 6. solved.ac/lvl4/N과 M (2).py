from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

# 1. 백트래킹


def dfs(start):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(start, n+1):
        if not i in arr:  # 조합
            arr.append(i)
            dfs(i+1)
            arr.pop()


dfs(1)

# 2. 모듈 사용
for case in combinations(range(1, n+1), m):
    case = list(case)
    for i in case:
        print(i, end=' ')
    print()
