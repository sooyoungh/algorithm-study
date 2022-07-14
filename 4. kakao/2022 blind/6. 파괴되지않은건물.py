# 2차원 누적합
def solution(board, skill):
    row = len(board)
    col = len(board[0])
    answer = 0
    graph = [[0] * (col + 1) for _ in range(row + 1)]

    # 누적합 시작/종료 지점 표시
    for type, r1, c1, r2, c2, degree in skill:
        graph[r1][c1] += degree if type == 2 else -degree
        graph[r1][c2 + 1] += -degree if type == 2 else degree
        graph[r2 + 1][c1] += -degree if type == 2 else degree
        graph[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    # 행 기준
    for i in range(row):
        for j in range(col):
            graph[i][j + 1] += graph[i][j]

    # 열 기준
    for j in range(col):
        for i in range(row):
            graph[i + 1][j] += graph[i][j]

    # 기존 배열과 합
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += graph[i][j]
            if board[i][j] > 0:
                answer += 1

    print(answer)

    return answer
