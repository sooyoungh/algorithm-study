# ING ...
# 테케 1만 통과

from itertools import product
import heapq
import copy
m, s = map(int, input().split())
# graph = [[None]*4 for i in range(4)] 
graph = [[ [] for _ in range(4)] for _ in range(4)] # 한 칸에 여러 물고기가 존재할 수 있음
smell = [[0]*4 for i in range(4)] # 숫자가 의미 있음

fish_pos = []
for i in range(m):
    x,y,d = map(int, input().split())
    graph[x-1][y-1].append(d-1)
    fish_pos.append([x-1,y-1,d-1])

now_x, now_y = map(int, input().split())
now_x -= 1
now_y -= 1

# 0 1  2  3  4 5  6  7
# ←,↖,↑,↗, →,↘,↓,↙  
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
            
def turn(d):
    d = (d - 1)%8
    return d

# 1. 물고기 이동
def move_fish():
    global graph, fish_pos
    new_fish_pos = []
    for case in fish_pos:
        x,y,d = case
        prev_d = d
        for i in range(8): # 방향이 회전하는 경우 - 최초는 그대로 유지해야함 -> turn 함수 빼기
            # 이동은 처음부터
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4: # 격자의 범위를 벗어나는 칸인지?
                if nx != now_x or ny != now_y: # 상어가 있는 칸인지?
                    if smell[nx][ny] == 0: # 물고기의 냄새가 있는 칸인지?
                        # 가능한 칸인 경우 - 해당 위치 추가
                        graph[nx][ny].append(d)
                        new_fish_pos.append([nx,ny,d])
                        graph[x][y].remove(prev_d)
                        break
            # 회전은 두번째부터
            d = turn(d)
    return new_fish_pos, fish_pos

dx_shark = [0,-1,0,1,0]
dy_shark = [0,0,-1,0,1]

# 2. 상어 이동
def move_shark():
    global graph, now_x, now_y, smell, fish_pos

    # 사전 순서로 가장 많이 먹을 수 있는 방향셋 구하기
    eat_fish = []
    for direction in product(range(1,5), range(1,5), range(1,5)):
        tmp = copy.deepcopy(graph)
        eat_cnt = 0
        flag = True
        nx, ny = now_x, now_y
        for i in direction:
            nx = nx + dx_shark[i]
            ny = ny + dy_shark[i]
            if not (0 <= nx < 4 and 0 <= ny < 4): # 범위 벗어나면 이동 불가
                flag = False
                break
            if len(tmp[nx][ny]) != 0 :
                eat_cnt += len(tmp[nx][ny]) # 똑같은 걸 두번 먹어서 틀림
                tmp[nx][ny] = []
        if flag == True:
            if eat_cnt != 0 :
                heapq.heappush(eat_fish, ( -1 * eat_cnt, direction))

    eat_cnt, direction = heapq.heappop(eat_fish)

    # 해당 방향으로 이동 가능하면
    for i in direction:
        now_x = now_x + dx_shark[i]
        now_y = now_y + dy_shark[i]
        if len(graph[now_x][now_y]) != 0 :
            graph[now_x][now_y] = []
            smell[now_x][now_y] = 2

    for k in fish_pos:
        a,b,c = k
        if a == now_x and b == now_y:
            fish_pos.remove((a,b,c))
    
# 3. 복제
def copy_fish(prev_fish):
    global graph
    for case in prev_fish:
        x,y,d = case
        graph[x][y].append(d)

# 4. smell
def smell_cnt():
    global smell
    for i in range(4):
        for j in range(4):
            if smell[i][j] != 0:
                smell[i][j] -= 1

# s번 반복
for _ in range(s):

    # 1. 물고기 복제 & 물고기 이동
    fish_pos, prev_fish = move_fish()
    # 2. 상어 이동
    move_shark()
    # 3. 복제
    copy_fish(prev_fish)

    smell_cnt()

result = 0
for i in range(4):
    for j in range(4):
        if not (i == now_x and j == now_y): #상어가 없는 쪽
            if len(graph[i][j]) != 0:
                result += len(graph[i][j])

print(result)
