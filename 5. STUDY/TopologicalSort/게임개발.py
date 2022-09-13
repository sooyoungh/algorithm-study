from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

indegree = [0]*(n+1)
data = [[] for _ in range(n + 1)]
time = [0] * (n+1)

for i in range(1, n+1):
    tmp = list(map(int, input().split()))[:-1]
    time[i] = tmp[0]  # 정점
    for j in tmp[1:]:  # 해당 정점을 만들기 위해 먼저 만들어야하는 정점들
        data[j].append(i)  # j -> i
        indegree[i] += 1  # i 만들기전에 몇건물이 먼저 만들어져야되는지

answer = [0]*(n+1)
q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    answer[now] += time[now]  # 해당 건물 시간 추가 (맨앞, 마지막은 자기 시간만 더하고 끝남!)
    for after in data[now]:  # 다음 건물들에도 값 갱신
        indegree[after] -= 1
        answer[after] = max(answer[now], answer[after])
        if indegree[after] == 0:
            q.append(after)

for i in answer[1:]:
    print(i)
