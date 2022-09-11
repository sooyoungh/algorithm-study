# BFS + 이분탐색
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 공장 두개
start, end = map(int, input().split())

#  이 중량제한으로 옮길 수 있는 지?


def bfs(tmp_cost):
    q = deque()
    q.append(start)
    visited = set()
    visited.add(start)
    while q:
        now = q.popleft()
        for b, cost in graph[now]:
            if b not in visited and cost >= tmp_cost:
                q.append(b)
                visited.add(b)

    if end in visited:
        return True
    else:
        return False


# 중량 최소/최대
MIN = 1
MAX = 1000000000

# 이분 탐색
result = MIN
while MIN <= MAX:
    mid = (MIN+MAX)//2
    if bfs(mid):
        result = mid
        MIN = mid + 1
    else:
        MAX = mid - 1

print(result)
