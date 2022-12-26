from itertools import product
import copy
tc = int(input())

move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

answer = 0


def start():
    n, m, k = map(int, input().split())
    graph = []
    graph.append([0]*(m+1))
    for _ in range(n):
        data = [0] + list(map(int, input().split()))
        graph.append(data)

    result = []

    # !!!!!중복 순열 수정!!
    for i in product(range(4), repeat=k):
        result.append(i)

    def find_max(new_graph):
        max_result = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if new_graph[i][j] > max_result:
                    max_result = new_graph[i][j]
        return max_result

    def wind(d, new_graph):
        if d == 0:  # 서 -> 동
            x_start, x_end, dis_x = 1, n+1, 1
            y_start, y_end, dis_y = 1, m+1, 1
        elif d == 1:  # 동 -> 서
            x_start, x_end, dis_x = 1, n+1, 1
            y_start, y_end, dis_y = m, -1, -1
        elif d == 2:  # 북 -> 남
            x_start, x_end, dis_x = 1, n+1, 1
            y_start, y_end, dis_y = 1, m+1, 1
        else:  # 남 -> 북
            x_start, x_end, dis_x = n, -1, -1
            y_start, y_end, dis_y = 1, m+1, 1

        if d == 0 or d == 1:
            for x in range(x_start, x_end, dis_x):
                for y in range(y_start, y_end, dis_y):
                    if new_graph[x][y] != 0:  # 첫번째 숫자를 만날 때까지
                        nx = x + move[d][0]
                        ny = y + move[d][1]
                        if 0 < nx <= n and 0 < ny <= m:
                            new_graph[nx][ny] += new_graph[x][y]
                            new_graph[x][y] = 0
                        break
        elif d == 2 or d == 3:  # 열 먼저
            for y in range(y_start, y_end, dis_y):
                for x in range(x_start, x_end, dis_x):
                    if new_graph[x][y] != 0:
                        nx = x + move[d][0]
                        ny = y + move[d][1]
                        if 0 < nx <= n and 0 < ny <= m:
                            new_graph[nx][ny] += new_graph[x][y]
                            new_graph[x][y] = 0
                        break

        return new_graph

    total_max = 0

    for move_order in result:  # (0,0,1)
        new_graph = copy.deepcopy(graph)
        for d in move_order:  # 0
            new_graph = wind(d, new_graph)
            new_max = find_max(new_graph)

            if new_max > total_max:
                total_max = new_max

    return total_max


answer = []
for i in range(tc):
    answer.append(start())


for i in range(tc):
    print("#", i+1, answer[i])
