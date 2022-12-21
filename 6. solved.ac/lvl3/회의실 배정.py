import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    start, end = map(int, input().split())
    data.append((start, end))

# 정렬
# 끝나는 시간, 시작 시간 순서대로 정렬
data.sort(key=lambda x: (x[1], x[0]))

last = data[0][1]
cnt = 1
for i in range(1, n):
    if data[i][0] >= last:
        cnt += 1
        last = data[i][1]

print(cnt)
