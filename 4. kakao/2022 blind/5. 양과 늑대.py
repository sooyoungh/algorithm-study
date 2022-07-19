# 모든 경로 다 방문 후 max값 찾기
# 1) DFS
def solution(info, edges):

    def find_child(node):
        tmp = []
        for par, child in edges:
            if node == par:
                tmp.append(child)
        return tmp

    def dfs(sheep, wolf, current, path):
        if info[current]:
            wolf += 1
        else:
            sheep += 1

        if sheep <= wolf:
            return 0

        max_sheep = sheep

        for p in path:
            for n in find_child(p):  # 갈 수 있는 자식 노드들
                if n not in path:
                    path.append(n)
                    # 최대 양 판별
                    max_sheep = max(max_sheep, dfs(sheep, wolf, n, path))
                    path.pop()

        return max_sheep

    answer = dfs(0, 0, 0, [0])

    return answer


# 2) BFS
from collections import deque

def solution(info, edges):

    graph = [[] for _ in range(len(info))]
    max_sheep = 0

    for par, child in edges:
        graph[par].append(child)

    q = deque([[0, 1, 0, set()]])

    while q:
        now, sheep, wolf, record = q.popleft()
        max_sheep = max(max_sheep, sheep)
        # 현재 노드의 자식 노드들 추가
        for i in graph[now]:
            record.add(i)

        for child in record:
            # child로 이동가능하면 sheep혹은 wolf값 갱신해주고, 
            # 나머지 갈 수 있는 노드들 record - {child}
            if info[child]:  # 늑대
                if sheep != wolf + 1:
                    q.append([child, sheep, wolf+1, record - {child}])
            else:  # 양
                q.append([child, sheep+1, wolf, record - {child}])

    return max_sheep
