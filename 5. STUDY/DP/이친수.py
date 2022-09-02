import sys
input = sys.stdin.readline

n = int(input())

# 시작점
dp = [0, 1, 1]

# 경우의 수는 앞에 10붙인채
# 5자리수 = (10 + 앞자리 1빼고 4자리수) + (10 + 전체 3자리수)
# dp [i] = dp [i-1] + dp [i-2]

for i in range(3, 91):
    dp.append(dp[i-1] + dp[i-2])

print(dp[n])
