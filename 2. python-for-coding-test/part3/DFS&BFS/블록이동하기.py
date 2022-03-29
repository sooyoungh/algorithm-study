from collections import deque

def get_next(pos, new_board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 1. 상하좌우로 이동하는 경우
    for i in range(4):
        pos1_x_next = pos1_x + dx[i]
        pos1_y_next = pos1_y + dx[i]
        pos2_x_next = pos2_x + dy[i]
        pos2_y_next = pos2_y + dy[i]
        if new_board[pos1_x_next][pos1_y_next] == 0 and new_board[pos2_x_next][pos2_y_next] == 0:
            next_pos.append({(pos1_x_next, pos1_y_next), (pos2_x_next, pos2_y_next)})
    # 2. 로봇이 회전하는 경우
    if pos1_x == pos2_x: # 로봇이 가로로 있는 경우
        for i in [-1,1]:
            if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] ==0 :
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i,pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i,pos2_y)})
    elif pos1_y == pos2_y: # 로봇이 세로로 있는 경우
        for i in [-1,1]:
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] ==0 :
                next_pos.append({(pos1_x, pos1_y), (pos1_x ,pos1_y+i )})
                next_pos.append({(pos2_x, pos2_y), (pos2_x ,pos2_y+i )})
    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    q = deque()  # 다음 연결 노드 보기
    visited = []  # 방문 처리

    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get(pos, nex_board):  # 이 부분이 복잡해짐
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0
