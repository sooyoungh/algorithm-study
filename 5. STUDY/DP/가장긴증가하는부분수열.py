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

# 2) 이분 탐색
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
answer = [0]  # 증가 수열

for case in data:
    if answer[-1] < case:  # 증가하면 증가수열에 추가
        answer.append(case)
    else:  # 아니면 위치 체크
        left = 0
        right = len(answer)

        while left < right:
            mid = (right+left)//2
            if answer[mid] < case:
                left = mid+1
            else:
                right = mid
        answer[right] = case

print(len(answer)-1)
