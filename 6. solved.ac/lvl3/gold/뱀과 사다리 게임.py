from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [i for i in range(101)]  # 기본(최대 횟수) : 주사위를 1번씩 돌려 나온 횟수
min_dice = [0] * 101  # 해당 칸에 도착할 떄의 최소 주사위 횟수 기록용

for _ in range(n+m):
    x, y = map(int, input().split())
    graph[x] = y

q = deque([1])
min_dice[1] = 1 # 0이면 한번도 방문 안한 것과 같아 아래 조건문에서 걸리므로 1로 셋팅 후 나중에 -1

new = 0
while q and new != 100:  # 100번까지 도착했으면 종료
    now = q.popleft()
    for i in range(1, 7):
        new = now + i
        if new > 100:
            continue
        new = graph[new]  # 사다리/뱀으로 이동할 수 있는 경우
        if not min_dice[new]:
            q.append(new)
            min_dice[new] = min_dice[now] + 1

print(min_dice[100]-1)
