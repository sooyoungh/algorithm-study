# 누적합 2차원
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 배열 정보
graph = [[0]*(n+1) for _ in range(n+1)]
new_graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n+1):
    for j in range(1, n+1):
        graph[i][j] = new_graph[i-1][j-1]

data = [list(map(int, input().split())) for _ in range(m)]

# 행 누적합
for i in range(1, n+1):
    for j in range(1, n):
        graph[i][j+1] += graph[i][j]

# 열 누적합
for i in range(1, n):
    for j in range(1, n+1):
        graph[i+1][j] += graph[i][j]


# 값 구하기
for case in data:
    x1, y1, x2, y2 = case

    # 총 누적합
    tmp = graph[x2][y2] - graph[x1-1][y2] - graph[x2][y1-1] + graph[x1-1][y1-1]
    # 행/열 합 빼기
    # 중복되어 2번 뺀 누적합 한번 더하기

    print(tmp)
