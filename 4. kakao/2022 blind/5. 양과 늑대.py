# 모든 경로 다 방문 후 max값 찾기
# 1) DFS - 내풀이
def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    max_sheep = 0

    for par, next in edges:
        graph[par].append(next)

    def dfs(sheep, wolf, now, path):
 
       if info[now] == 0:  # 양
            sheep += 1
        else:  # 늑대
            wolf += 1
            if sheep <= wolf: # 양 < 늑대인 경우, dfs 탐색 멈춤
                return -1

        max_sheep = sheep
        
        # 현재 노드 now
        for child in graph[now]: # 이미 8번 있는데, 1번의 자식들 (2,4번) 추가
            path.add(child) # set
        path.discard(now) # 현재 노드 now 삭제! (여기)
        
        for node in path: # 8번 / 2번 4번
            new_path = path.copy()
            # new_path.remove(node) 없어도 됨! => dfs 내부에서 현재 시작 노드(now)를 삭제해주기에
            # 위 방식만으로는 최초의 dfs(0, 0, 0, set([0]))에서 path값 set([0])에서 0노드를 삭제해주지 못하므로
            # 이 루프 전에 (여기)에서 삭제처리 해주어어야 함
            max_sheep = max(max_sheep, dfs(sheep, wolf, node, new_path))
                    
        return max_sheep

    answer = dfs(0, 0, 0, set([0]))

    return answer




# 2) BFS
from collections import deque
import copy


def solution(info, edges):

    graph = [[] for _ in range(len(info))]
    max_sheep = 0

    for par, child in edges:
        graph[par].append(child)

    q = deque([[0, 0, 0, set([0])]])

    while q:
        now, sheep, wolf, path = q.popleft()

        # 1) 현재 노드 now를 path에서 삭제
        path.remove(now)
        
        # 2) 양과 늑대 조건 체크
        if info[now]:
            wolf += 1
            if sheep <= wolf:  # 양 < 늑대인 경우, bfs 멈춤
                continue
        else:
            sheep += 1
            
        max_sheep = max(max_sheep, sheep) # !!답 체크는 양/늑대 만족 후에!!

        # 3) 현재 노드 now의 자식들을 path에 추가
        for i in graph[now]:
            path.add(i)

        # 4)  bfs 큐에 추가
        for node in path:
            new_path = copy.deepcopy(path)
            q.append([node, sheep, wolf, new_path])

    return max_sheep





# --------------------추가---------------------------
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
