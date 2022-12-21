from collections import deque
import sys
input = sys.stdin.readline

visited = [0] * (10**5 + 1)  # 최초로 찾을 떄만 중요! => 처음 찾았을 때의 횟수만 기록하기
n, k = map(int, input().split())


def bfs():
    q = deque([n])
    while q:
        now = q.popleft()
        if now == k:
            print(visited[now])
            break
        for new_n in (now-1, now+1, 2*now):
            if 0 <= new_n <= 10**5 and not visited[new_n]:
                visited[new_n] = visited[now] + 1
                q.append(new_n)


bfs()
