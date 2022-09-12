import heapq
import sys
input = sys.stdin.readline
INF = 1e9

v, e = map(int, input().split())
distance = [INF] * (v+1)
start = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


q = []


def dijkstra(start):
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cur_d, cur_n = heapq.heappop(q)
        if distance[cur_n] < cur_d:
            continue
        for new_n, new_d in graph[cur_n]:
            sum_dist = cur_d + new_d
            if sum_dist < distance[new_n]:
                distance[new_n] = sum_dist
                heapq.heappush(q, (sum_dist, new_n))


dijkstra(start)


for dist in distance[1:]:
    if dist != INF:
        print(dist)
    else:
        print("INF")
