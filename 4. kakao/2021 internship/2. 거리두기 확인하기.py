# 1. BFS
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(start_x, start_y, graph):
    visited = [[False]*5 for _ in range(5)]
    visited[start_x][start_y] = True
        
    q = deque()
    q.append([start_x, start_y, 0])
        
    while q:
        x, y, index = q.popleft()
        if index == 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5: 
                if not visited[nx][ny]: # 원래의 P일 경우 + O을 또 방문할 경우 제외하기
                    if graph[nx][ny] == 'P':
                        return False
                    if graph[nx][ny] == 'O':
                        q.append([nx,ny,index+1])
                        visited[nx][ny] = True
    return True


def solution(places):
    answer = []

    for i in range(5):
        graph = places[i]
        flag = 1
        
        for x in range(5):
            for y in range(5):
                if graph[x][y] == 'P':
                    if not bfs(x,y, graph):
                        flag = False
            if flag == False:
                break
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer


# 2. 
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(array, start_x, start_ay):
    visited = [[False]*5 for _ in range(5)]
    flag = True
    q = deque()
    q.append((0, (start_x, start_ay)))

    while q:
        dist, (x, y) = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if not visited[nx][ny]:  # O을 또 방문할 경우 제외하기
                    if array[nx][ny] == 'O' and dist < 2:
                        q.append((dist+1, (nx, ny)))
                        visited[nx][ny] = True
                    if array[nx][ny] == 'P' and dist < 2:
                        flag = False
                        return flag
    return flag


def solution(places):
    answer = []

    for i in range(5):
        array = places[i]
        flag = 1

        for i in range(5):
            for j in range(5):
                if array[i][j] == 'P':
                    if not bfs(array, i, j):
                        flag = 0
                        break
            if not flag:  # 이중 for 문이므로 여기서 break!
                break

        answer.append(flag)

    return answer

