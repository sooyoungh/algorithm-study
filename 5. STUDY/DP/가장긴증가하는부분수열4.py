# DP
import sys
from unittest import result
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)

length = max(dp)
print(length)
result = []

for i in range(n-1, -1, -1):
    if length == dp[i]:
        result.append(data[i])
        length -= 1

result.sort()

for i in result:
    print(i, end=" ")
