import sys
input = sys.stdin.readline

# Q) 최소 c명이상 일때의 최소 비용?
c, n = map(int, input().split())

# 홍보비, 얻는 손님수
data = [list(map(int, input().split())) for _ in range(n)]

data.sort()

# 1000대신, c+100 이어도 괜찮음!
dp = [1e9] * (c+100)
dp[0] = 0

for ad_cost, ad_cus in data:
    for cus in range(ad_cus, c+100):
        # dp[현재 손님수] = min (dp[현재 손님수 - 홍보 손님수 ] + 홍보 비용, dp[현재 손님수] )
        dp[cus] = min(dp[cus], ad_cost + dp[cus - ad_cus])

print(min(dp[c:]))
