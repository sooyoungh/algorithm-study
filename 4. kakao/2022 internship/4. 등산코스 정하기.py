import heapq


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))

    min_intensity = [1e9] * (n+1)

    q = []

    # 시작점(출입구)
    for gate in gates:
        heapq.heappush(q, (0, gate))
        min_intensity[gate] = 0

    while q:
        now_int, now = heapq.heappop(q)
        if min_intensity[now] < now_int:  # 이 길로는 갈 필요X
            continue
        min_intensity[now] = now_int
        if now in summits:
            continue
        for next, next_d in graph[now]:
            new_int = max(now_int, next_d)  # intensity 업데이트
            if min_intensity[next] > new_int:
                min_intensity[next] = new_int
                heapq.heappush(q, (new_int, next))

    answer = [0, 1e9]

    # 지점 번호 작은 것부터 정렬 -> 같은 intensuty면 지점 번호 작을 때만 업데이트!
    summits.sort()
    for summit in summits:
        if answer[1] > min_intensity[summit]:
            answer[0] = summit
            answer[1] = min_intensity[summit]

    return answer


n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4],
         [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]

print(solution(n, paths, gates, summits))
