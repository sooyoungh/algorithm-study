import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = 1e9

graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = min(cost, graph[a][b])

# 거쳐가는 경로 k를 먼저래야 누락이 없음
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
            else:
                # k를 거쳐 가는 게 빠르다면 갱신
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for row in graph[1:]:  # 행마다
    for node in row[1:]:
        if node == INF:
            print(0, end=" ")
        else:
            print(node, end=" ")
    print()
