
from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())


def bfs(start, end):
    q = deque([(start, "")])
    visited = [0] * 10000
    visited[start] = 1
    while q:
        cur_n, ops = q.popleft()

        if cur_n == end:
            return ops

        if not visited[(cur_n*2) % 10000]:
            visited[(cur_n*2) % 10000] = 1
            q.append(((cur_n*2) % 10000, ops+"D"))
        if not visited[(cur_n-1) % 10000]:
            visited[(cur_n-1) % 10000] = 1
            q.append(((cur_n-1) % 10000, ops+"S"))
        # L연산 : d2, d3, d4은 1000의 나머지로 구하기 + d1은 1000으로 나눠서 구하기
        if not visited[cur_n % 1000 * 10 + cur_n//1000]:
            visited[cur_n % 1000 * 10 + cur_n//1000] = 1
            q.append((cur_n % 1000 * 10 + cur_n//1000, ops+"L"))
        # R 연산 : d4는 10으로 나눈 몫으로 구하기 + d1, d2, d3은 10으로 나눠서 구하기
        if not visited[cur_n % 10 * 1000 + cur_n // 10]:
            visited[cur_n % 10 * 1000 + cur_n // 10] = 1
            q.append((cur_n % 10 * 1000 + cur_n // 10, ops+"R"))


for _ in range(tc):
    a, b = map(int, input().split())
    print(bfs(a, b))
