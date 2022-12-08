# 1-------딕셔너리--------
from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

m = int(input())
find = list(map(int, input().split()))

data_dict = defaultdict(int)
for i in data:
    data_dict[i] += 1

answer = []
for target in find:
    ans = data_dict[target]
    print(ans, end=' ')

# 2--------이분 탐색--------
