import sys
input = sys.stdin.readline

# Q) 최소 c명이상 일때의 최소 비용?
c, n = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
data.sort()

dp = [1e9] * (c + 100)
dp[0] = 0
for cost, cus in data:
    for i in range(cus, c + 100):
        # dp[현재 손님수] = min (dp[현재 손님수], dp[현재 손님수 - 홍보 손님수 ] + 홍보 비용 )
        dp[i] = min(dp[i], dp[i-cus] + cost)

print(min(dp[c:]))
