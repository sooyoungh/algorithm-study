import heapq
import sys
input = sys.stdin.readline

n = int(input())

# 우선 순위 큐 - 오름차순
q = []
for _ in range(n):
    command = int(input())
    if command == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, command)
