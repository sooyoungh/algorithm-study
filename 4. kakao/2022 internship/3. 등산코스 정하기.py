import heapq


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # heapq 시작은 출입구만!
    q = []
    for gate in gates:
        heapq.heappush(q, (0, gate))

    # 각 노드까지의 최소 intensity
    min_intensity = [1e9 for _ in range(n+1)]

    while q:
        cur_intensity, cur = heapq.heappop(q)
        if min_intensity[cur] <= cur_intensity:  # 이미 최소면 패스
            continue
        min_intensity[cur] = cur_intensity
        if cur in summits:
            continue
        for next, dist in graph[cur]:
            next_intensity = max(dist, min_intensity[cur])
            if min_intensity[next] > next_intensity:
                heapq.heappush(q, (next_intensity, next))

    answer = [0, 1e9]
    summits.sort()  # 산봉우리 순서대로 정렬

    for summit in summits:
        if min_intensity[summit] < answer[1]:  # intensity가 작을 때만 업데이트, 같으면 예외
            answer[0] = summit
            answer[1] = min_intensity[summit]

    return answer


n = 7
paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
gates = [1]
summits = [2, 3, 4]

print(solution(n, paths, gates, summits))
