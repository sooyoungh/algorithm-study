import heapq
import sys
input = sys.stdin.readline

tc = int(input())


def start():
    n = int(input())
    q = []

    for _ in range(n):
        command, num = input().split()
        num = int(num)
        if command == 'I':
            heapq.heappush(q, num)
        else:
            if len(q) == 0:
                continue
            if num == -1:  # 최소값 삭제
                heapq.heappop(q)
            else:
                new_q = heapq.nlargest(1, q)[1:]  # 최대값 삭제
                heapq.heapify(new_q)
                q = new_q

    if len(q) == 0:
        print("EMPTY")
    else:
        print(max(q), min(q))


for _ in range(tc):
    start()
