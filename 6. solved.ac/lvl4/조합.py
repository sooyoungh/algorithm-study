import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

# 1. 파스칼의 삼각형 - DP
# m개의 조합수 = m-1개의 조합에서 m번째 수를 뽑느냐 마느냐 경우의 수를 합친거
# dp[n][m] = dp[n-1][m-1] + dp[n-1][m]
dp = [[0 for _ in range(101)] for _ in range(101)]
for i in range(1, 101):
    dp[i][0] = 1  # iC0
    dp[i][i] = 1  # iCi

for i in range(2, 101):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][m])

# 2. fac 정의 그대로 n! / (n-m)! * m!
result = math.factorial(n) // (math.factorial(n-m) * math.factorial(m))


def fac(n):
    answer = 1
    for i in range(2, n+1):
        answer *= i
    return answer
