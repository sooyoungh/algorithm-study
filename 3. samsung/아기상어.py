# 매번 상어가 물고기 먹고 나면 => while 반복문
# 한 노드에서 다른 노드까지의 최단 거리 구해야함 => BFS로 함수로 빼놓음

# graph 2차원 배열 : 데이터 기록용
# dist 2차원 배열 : 최단 거리 계산 기록용
# q 큐 : 지금 노드에 연결된 (이동가능한) 다른 노드들

from collections import deque
INF = 1e9
graph = []
n = int(input())
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[i][j] = 0

now_size = 2
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 현재 시작 노드에서 모든 노드까지의 최단 거리 계산
def bfs():
    dist = [[-1] * n for _ in range(n)]
    q = deque([now_x, now_y])
    dist[now_x, now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1 and graph[nx][ny] < now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= graph < now_size:
                x, y = i, j
                min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist


result = 0
ate = 0

# 매번 최단 거리를 구해야하는 경우,,
while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0],  value[1]
        result += value[2]
        graph[now_x][now_y] = 0
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0
