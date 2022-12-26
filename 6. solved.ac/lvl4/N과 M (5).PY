import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()


def dfs(tmp):
    if len(tmp) == m:
        print(" ".join(map(str, tmp)))
        return
    for i in arr:
        if not i in tmp:
            tmp.append(i)
            dfs(tmp)
            tmp.pop()


dfs([])
