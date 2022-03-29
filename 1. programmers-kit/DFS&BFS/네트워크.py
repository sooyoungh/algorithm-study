# 1. DFS 풀이
def dfs(n, case, computers, visited ):
    # visited가 파라미터로 들어오면 nonlocal 하면 안됨, 그냥 수정가능
    visited[case] = True
    for i in range(n):
        if i == case:
            continue
        if computers[case][i] == 1 and visited[i] == False:
            dfs(n, i, computers, visited )

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for case in range(n):
        if visited[case] == False:
            dfs(n, case, computers, visited )
            answer += 1
    
    return answer
  
# 2. BFS
from collections import deque
def bfs(n, start, visited, computers):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for i in range(n):
            if i == now:
                continue
            if computers[now][i] == 1 and visited[i] == False:
                visited[i] = True
                q.append(i)

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] == False:
            bfs(n, i, visited, computers)
            answer += 1
    
    return answer
