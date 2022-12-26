import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            tmp = dp[j] + 1
            dp[i] = max(dp[i], tmp)

max_len = max(dp)

print(max_len + 1)

# 수열 출력하기
# answer = []
# for i in range(n-1, -1, -1):
#     if dp[i] == max_len:
#         answer.append(arr[i])
#         max_len -= 1

# answer.sort()
# print(answer)
