import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    a, b = a - 1, b-1
    graph[a].append((cost, b))

start, end = map(int, input().split())

start -= 1
end -= 1
q = []
distance = [1e9] * (n)


def dijk(x):
    heapq.heappush(q, (0, x))
    distance[x] = 0

    while q:
        now_d, now_n = heapq.heappop(q)
        if now_d > distance[now_n]:
            continue
        for next_d, next_n in graph[now_n]:
            sum_d = now_d + next_d
            if sum_d < distance[next_n]:
                distance[next_n] = sum_d
                heapq.heappush(q, (sum_d, next_n))


dijk(start)
print(distance[end])
