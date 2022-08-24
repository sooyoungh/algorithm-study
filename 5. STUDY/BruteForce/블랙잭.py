# 조합
import sys
from itertools import combinations
input = sys.stdin.readline


n, m = map(int, input().split())
arr = list(map(int, input().split()))
data = list(combinations(arr, 3))

result = 0
for case in data:
    tmp = sum(case)
    if tmp > m:
        continue
    result = max(result, tmp)

print(result)
