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
