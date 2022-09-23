# 1) DP
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dp = [1] * (n) # 초기화

for i in range(n):  # i일때
    for j in range(i):  # i전까지의 원소들을 비교했을때
        if data[i] > data[j]:  # 증가수열이라면
            dp[i] = max(dp[i], dp[j]+1)  # 짧은 증가수열값이 이미 update되어 있을 수 있으니, max 비교해서 바꿔주기

print(max(dp))

# 2) 이분 탐색 !!
