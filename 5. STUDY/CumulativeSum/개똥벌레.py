# 누적합
import sys
input = sys.stdin.readline

n, h = map(int, input().split())

floor = [0] * h  # 아래에서부터 (석순)
ceil = [0] * h  # 위에서부터 (종유석)

for i in range(n):
    tmp = int(input())
    if i % 2 == 0:  # 아래에서부터 (석순)
        floor[tmp-1] += 1
    else:  # 위에서부터 (종유석)
        ceil[tmp-1] += 1

for i in range(h-1, 0, -1):
    floor[i-1] += floor[i]
    ceil[i-1] += ceil[i]

min_val = 1e9
result = 0

for i in range(h):
    tmp = floor[i] + ceil[h-i-1]
    if tmp < min_val:
        min_val = tmp
        result = 0
    if tmp == min_val:
        result += 1

print(min_val, result)
