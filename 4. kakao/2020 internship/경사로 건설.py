# 1. BFS
from collections import deque

def solution(board):
    state = ''
    n = len(board)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[0] * n for _ in range(n)]
    costs = [[1e9] * n for _ in range(n)]

    q = deque()
    visited[0][0] = 1
    costs[0][0] = 0

    if board[0][1] == 0:
        q.append(('horizontal', 100, (0, 1)))
        visited[0][1] = 1
        costs[0][1] = 100

    if board[1][0] == 0:
        q.append(('vertical', 100, (1, 0)))
        visited[1][0] = 1
        costs[1][0] = 100

    while q:
        state, cost, now = q.popleft()
        x, y = now
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    new_state = 'vertical' if abs(nx-x) == 1 else 'horizontal'
                    new_cost = cost + 100 if state == new_state else cost + 600
                    if new_cost <= costs[nx][ny]:
                        costs[nx][ny] = new_cost
                        q.append((new_state, new_cost, (nx, ny)))

    return costs[-1][-1]

# 2. 개선해야할 풀이
from collections import deque

VERT = 0
HORI = 1
INF = 1e9

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(board):
    n = len(board)
    visited = [[INF]*n for _ in range(n)]

    q = deque()
    q.append((0, 0, VERT, 0))
    q.append((0, 0, HORI, 0))

    visited[0][0] = 0

    while q:
        x, y, state, cost = q.popleft()

        if x == n-1 and y == n-1:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    if abs(nx-x) == 0 and abs(ny-y) == 1:
                        new_state = HORI
                    elif abs(nx-x) == 1 and abs(ny-y) == 0:
                        new_state = VERT

                    if state == new_state:
                        new_cost = cost + 100
                    else:
                        new_cost = cost + 600
                    # 저장된 cost보다 적을 경우에만 더 탐색..! -> 이래야 시간초과 안남
                    if new_cost < visited[nx][ny]:
                        q.append((nx, ny, new_state, new_cost))
                        visited[nx][ny] = new_cost

    return visited[n-1][n-1]


def solution(board):
    print(bfs(board))

    min_result = bfs(board)
    return min_result
