import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] * (m+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 다익스트라
cabin_bacon = defaultdict(int)
q = []


# 1. 한 노드에서 다른 모든 노드까지의 거리 구하기
def dijk(start, distance):
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cur_d, cur_n = heapq.heappop(q)
        if distance[cur_n] < cur_d:
            continue
        for new_n in graph[cur_n]:
            sum_d = cur_d + 1
            if sum_d < distance[new_n]:
                distance[new_n] = sum_d
                heapq.heappush(q, (sum_d, new_n))


# 2. 딕셔너리 총합 구하기 - 최소 체크
min_result = 1e9
for i in range(1, n+1):
    distance = [1e9] * (n+1)
    dijk(i, distance)
    distance[0] = 0
    sum_d = sum(distance)
    cabin_bacon[i] = sum_d
    if sum_d < min_result:
        min_result = sum_d

# 3. 딕셔너리 가장 작은 값 구하기
for i in range(1, n+1):
    if cabin_bacon[i] == min_result:
        print(i)
        break
