
import heapq
import sys
input = sys.stdin.readline
INF = 1e9

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

# 정거장
station1, station2 = map(int, input().split())

# 매번 시작-끝점의 최단 거리 구하기


def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cur_d, cur_n = heapq.heappop(q)
        if distance[cur_n] < cur_d:
            continue
        for new_n, new_d in graph[cur_n]:
            sum_d = cur_d + new_d
            if sum_d < distance[new_n]:
                distance[new_n] = sum_d
                heapq.heappush(q, (sum_d, new_n))
    return distance


start_dist = dijkstra(1)
station1_dist = dijkstra(station1)
station2_dist = dijkstra(station2)

case1 = start_dist[station1] + station1_dist[station2] + station2_dist[n]
case2 = start_dist[station2] + station2_dist[station1] + station1_dist[n]

answer = min(case1, case2)
print(answer if answer < INF else -1)
