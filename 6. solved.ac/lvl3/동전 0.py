import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)

answer = 0
while k > 0:
    for coin in coins:
        if coin > k:
            continue
        if k // coin > 0:
            answer += k // coin
            k %= coin

print(answer)
