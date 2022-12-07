from itertools import combinations
# n, m = 5, 21
# data = [5, 6, 7, 8, 9]
n, m = map(int, input().split())
data = list(map(int, input().split()))

max_sum = 0
for com in list(combinations(data, 3)):
    tmp_sum = sum(com)
    if tmp_sum <= m:
        max_sum = max(tmp_sum, max_sum)

print(max_sum)
