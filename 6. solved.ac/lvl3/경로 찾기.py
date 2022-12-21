import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 플로이드 -> 모든 노드에서 모든 노드까지의 거리
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()
