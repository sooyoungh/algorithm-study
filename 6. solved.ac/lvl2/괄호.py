import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(input().rstrip())

for tmp in data:
    cnt = 0
    for i in tmp:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break

    if cnt != 0:
        print("NO")
    else:
        print("YES")
