import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))


tmp = []  # dfs니까 한번에 하나 사용


def dfs(idx):
    if len(tmp) == m:
        print(" ".join(map(str, tmp)))
        return
    for i in range(idx, n):
        tmp.append(arr[i])
        dfs(i)
        tmp.pop()


dfs(0)
