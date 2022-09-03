
# 1) 1차원 DP : top-down
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

d = [0 for _ in range(k+1)]

for weight, value in data:
    for tmp in range(weight, k+1):  # 최대 k무게에서 1씩 줄이면서 weight까지
        if tmp >= weight:
            d[tmp] = max(d[tmp], value + d[tmp-weight])
    print(d)

print(d[-1])

# 2) 2차원 DP : bottom-up
input = sys.stdin.readline

n, k = map(int, input().split())
data = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    data.append(list(map(int, input().split())))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):  # 물건 루프
    for j in range(1, k+1):  # 무게 루프
        # 현재 물건(i)의 무게, 가치
        weight = data[i][0]
        value = data[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])

print(dp[n][k])
