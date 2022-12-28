import sys
input = sys.stdin.readline

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for depth in range(1, n):
    for index in range(depth+1):
        if index == 0:
            dp[depth][index] += dp[depth-1][index]
        elif index == depth:
            dp[depth][index] += dp[depth-1][index-1]
        else:
            dp[depth][index] += max(dp[depth-1][index-1], dp[depth-1][index])


print(max(dp[-1]))
