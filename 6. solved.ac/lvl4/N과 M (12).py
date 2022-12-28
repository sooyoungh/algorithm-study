import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
tmp = []
answer = []

#  중복 순열


def dfs():
    if len(tmp) == m:
        answer.append(tuple(tmp))
        return
    for i in data:
        if len(tmp) == 0 or tmp[-1] <= i:
            tmp.append(i)
            dfs()
            tmp.pop()


dfs()

answer = list(set(answer))
answer.sort()
for case in answer:
    print(" ".join(map(str, case)))
