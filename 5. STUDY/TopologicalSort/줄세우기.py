from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
q = deque()

for _ in range(m):
    # a < b
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 가장 작은 노드
for i in range(1, n+1):
    if indegree[1] == 0:
        q.append(i)

while q:
    tmp = q.popleft()  # indegree가 0 인 정점
    for next in graph[tmp]:
        indegree[next] -= 1  # 해당 정점과 대소비교한 점들 (작은 정점들)
        if indegree[next] == 0:
            q.append(next)
    print(tmp)
