from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())


def start():
    p = input()
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    q = deque(arr)

    if n == 0:
        q = deque()

    cnt_reverse = 0
    for i in p:
        if i == 'R':
            cnt_reverse += 1
        elif i == 'D':
            if len(q) == 0:
                return "error"
            elif cnt_reverse % 2 == 1:
                q.pop()
            else:
                q.popleft()

    if cnt_reverse % 2 == 1:
        q.reverse()
    return q


for _ in range(tc):
    q = start()
    if q == "error":
        print(q)
    else:
        q = ",".join(map(str, q))
        answer = "[" + q + "]"
        print(answer)
