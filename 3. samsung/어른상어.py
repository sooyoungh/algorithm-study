n,m,k = map(int, input().split())
# 처음상어 위치
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

#  1, 2, 3, 4
# 위, 아래, 왼쪽, 오른쪽
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 상어의 초기 방향 정해주기
direction = list(map(int, input().split()))

# m개의 행에 4개의 열에 배열 
# a) 3차원 배열인데 접근시 리스트로
# priority = [ [[] for _ in range(4)] for _ in range(m) ]
# for i in range(m):
#     for j in range(4):
#         tmp = list(map(int, input().split()))
#         priority[i][j].append(tmp)

# b) 2차원 배열
priority = []
for i in range(m):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priority.append(temp)

spell = [[[0,0]]*n for _ in range(n)]

# 상어 이동
def move_shark():
    # 이동한 그래프
    new_data = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if data[x][y] != 0:
                target_shark = data[x][y] # 상어번호
                cur_direction = direction[target_shark-1] # 이 상어 번호의 방향
                # 1. 주변에 냄새 없는 자리 있으면 이동
                move_possible = False 
                for i in priority[target_shark-1][cur_direction-1]:
                    # i : 1,2,3,4
                    nx = x + dx[i-1]
                    ny = y + dy[i-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if spell[nx][ny][1] == 0:
                            direction[target_shark-1] = i
                            # 상어 이동시키기
                            if new_data[nx][ny] == 0:
                                new_data[nx][ny] = data[x][y]
                            else :
                                new_data[nx][ny] = min(data[x][y], new_data[nx][ny])
                            move_possible = True
                            break
                if move_possible :
                    continue

                # 2. 주변에 모두 냄새가 남아있다면, 자신의 냄새가 있는 곳으로 이동
                for i in priority[target_shark-1][cur_direction-1]:
                    nx = x + dx[i-1]
                    ny = y + dy[i-1]
                    if 0<= nx < n and 0<= ny < n:
                        if spell[nx][ny][0] == target_shark:
                            direction[target_shark-1] = i
                            new_data[nx][ny] = data[x][y]
                            break
    return new_data

# 남은 상어가 몇마리인지 체크
def check():
    remain_shark = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] != 0:
                remain_shark += 1
    if remain_shark == 1:
        return True 
    return False

def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄새가 남아있는 경우
            if spell[i][j][1] > 0:
                spell[i][j][1] -= 1
            # 상어가 존재하는 위치의 경우
            if data[i][j] != 0:
                spell[i][j] = [data[i][j], k] # 상어번호랑 k

sec = 0
while True:
    sec += 1
    update_smell()
    data = move_shark() # 상어 이동 후 바뀐 그래프

    # 만약 남은 상어가 1마리이면 break
    if check():
        print(sec)
        break

    if sec >= 1000:
        print(-1)
        break
