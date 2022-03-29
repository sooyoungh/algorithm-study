import copy

array = [[None]*4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[j*2], data[j*2 + 1]-1]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def turn_left(d):
    return (d+1) % 8

result = 0

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j] == index:
                return (i, j)
    return None


def move(array, now_x, now_y):
    return


def possible(array, now_x, now_y):
    return positions


def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)

    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1

    # 1. 물고기 이동시키기
    move(array, now_x, now_y)

    # 2. 다음으로 연결된 노드들 찾아오기 =>  후에 for문에
    positions = possible(array, now_x, now_y)

    if len(possible) == 0:
        result = max(result, total)
        return
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)


dfs(array, 0, 0, 0)
print(result)
