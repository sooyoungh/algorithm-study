n = int(input())
length = n*n
data = []

for _ in range(length):
    data_input = list(map(int, input().split()))
    data.append(data_input)
# data = [list(map(int, input().split())) for _ in range(n**2)] 이렇게도 초기화

# 정렬 조건으로 한번에 해결
# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

graph = [[0]*(n+1) for _ in range(n+1)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for case in data:
    target = case[0]
    tmp = []  # 후보들, 후에 정렬
    for x in range(1, n+1):
        for y in range(1, n+1):
            if graph[x][y] == 0:
                like = 0
                blank = 0
                # 인접한 칸들
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 < nx <= n and 0 < ny <= n:
                        if graph[nx][ny] in case[1:]:
                            like += 1
                        if graph[nx][ny] == 0:
                            blank += 1
                tmp.append([like, blank, x, y])
    tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))  # 작은 게 먼저 정렬
    graph[tmp[0][2]][tmp[0][3]] = target

data.sort() # result 계산하기 위해서 번호순으로 정렬

result = 0
for x in range(1, n+1):
    for y in range(1, n+1):
        check = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 < nx <= n and 0 < ny <= n:
                if graph[nx][ny] in data[graph[x][y]-1]:
                    check += 1
        if check != 0:
            result += 10 ** (check-1)

print(result)
