import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
# 1. abs() 활용!
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(q, (abs(x), x))
    else:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
