# 누적합 + DP
import sys
input = sys.stdin.readline


n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())

# n대를 운행할 때, m번째 객차까지의 최대 손님수
# 최종 dp[n][m] 값이 답이다. (3대까지의 최대 손님수)
dp = [[0 for _ in range(n+1)] for _ in range(4)]

for i in range(1, 4):
    for j in range(m*i, n+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-m] + sum(arr[j-m+1: j+1]))

print(dp[3][n])
