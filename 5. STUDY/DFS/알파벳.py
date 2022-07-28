# 문자 그대로 대신에 
# 숫자로 저장하는게 탐색 더 빠름
# ord(x)-65
import sys
s = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, s().split())
graph = [list(map(lambda x: ord(x)-65, s())) for _ in range(n)]
visited = [0]*26


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_cnt = 0


def dfs(x, y, cnt):
    global max_cnt, visited
    if max_cnt < cnt:
        max_cnt = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            alpa = graph[nx][ny]
            if not visited[alpa]:
                visited[alpa] = 1
                dfs(nx, ny, cnt+1)
                visited[alpa] = 0


start_alpa = graph[0][0]
visited[start_alpa] = 1

cnt = 1
dfs(0, 0, cnt)

print(max_cnt)
