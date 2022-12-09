import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

answer = 0
for i in range(1, n+1):
    answer += sum(data[0:i])

print(answer)
