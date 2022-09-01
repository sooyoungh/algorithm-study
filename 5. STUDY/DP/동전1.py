# k원을 만드는 경우의 수!
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 최소 코인의 경우의 수 초기화 - 1차원 배열
dp = [1] + [0]*k

# 누적으로 경우의 수 더해주기
for coin in coins:
    for tmp in range(coin, k+1):
        if tmp >= coin:
            dp[tmp] += dp[tmp - coin]

print(dp[k])
