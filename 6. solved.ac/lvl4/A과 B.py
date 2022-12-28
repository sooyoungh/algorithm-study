from collections import deque
import sys
input = sys.stdin.readline

start, goal = map(int, input().split())
result = -1
q = deque([(start, 1)])

# 1. BFS
while q:
    num, cnt = q.popleft()
    if num == goal:
        result = cnt
        break
    num_case1 = num * 2
    num_case2 = num * 10 + 1
    if num_case1 <= goal:
        q.append((num_case1, cnt + 1))
    if num_case2 <= goal:
        q.append((num_case2, cnt + 1))

print(result)

# 2. top - down
cnt = 1
while True:
    if goal == start:
        break
    elif goal < start:
        cnt = -1
        break
    if goal % 10 == 1:
        goal //= 10
    elif goal % 2 == 0:
        goal //= 2
    else:  # 현재 어떤 연산도 못할 경우, break
        cnt = -1
        break
    cnt += 1

print(cnt)
