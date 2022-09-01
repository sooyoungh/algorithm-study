import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 초기화, 시작만 0으로 시작~!
dp = [10001] * (k+1)
dp[0] = 0

for coin in coins:
    for tmp in range(coin, k+1):
        dp[tmp] = min(dp[tmp], dp[tmp - coin] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
