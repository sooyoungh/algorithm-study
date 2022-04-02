import copy
#  ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

array = [[None]*4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[j*2], data[j*2+1]-1]


def find(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None


def turn_left(direction):
    return (direction + 1) % 8


def move(array, now_x, now_y):
    for i in range(1, 17):
        value = find(array, i)
        if value == None:
            continue
        x, y = value[0], value[1]
        direction = array[x][y][1]
        # 현재 방향으로 이동한 경우부터 체크
        for j in range(8):
            # direction = (direction+j) % 8 => 처음부터 0이되면 틀림
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == now_x and ny == now_y):  # 상어위치가 아니라면
                    array[x][y][1] = direction
                    array[nx][ny], array[x][y] = array[x][y], array[nx][ny]
                    break
            direction = turn_left(direction)

# DFS에서 상어가 이동할 수 있는 다음 노드 목록
def eat_fish(array, now_x, now_y):
    fishes = []
    direction = array[now_x][now_y][1]
    # 방향 회전 안하고 주어진 방향으로 계속 이동하기!
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if 0 <= now_x < 4 and 0 <= now_y < 4:
            if array[now_x][now_y][0] != -1:
                fishes.append((now_x, now_y))
    return fishes


result = 0


def dfs(now_x, now_y, total, array):
    global result
    array = copy.deepcopy(array)

    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1

    # 1. 물고기 대이동
    move(array, now_x, now_y)

    # 2. 상어가 먹을 물고기 리스트
    fish_list = eat_fish(array, now_x, now_y)

    # 3-1. 상어가 먹을 수 있는 물고기가 없으면 종료
    if len(fish_list) == 0:
        result = max(result, total)  # result는 이전 경우의 수 총합, total은 이번 경우의 총합
        return
    # 3-2. 있으면 for문으로 DFS돌림
    for next_x, next_y in fish_list:
        dfs(next_x, next_y, total, array)


dfs(0, 0, 0, array)
print(result)

# Tips*
# 값이 없을 경우 - None, len()
# gloabl result(전체 케이스의 max값), total(한 케이스) -> DFS에서 각 케이스의 모든 값을 구해서 최댓값을 구할 때 활용!
