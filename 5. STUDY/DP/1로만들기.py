import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1  # 1을 더하는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)  # 1을 더하는 경우 OR 3으로 나눈 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

print(d[n])
