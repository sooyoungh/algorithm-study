import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    # a < b
    a, b = map(int, input().split())
    graph[a][b] = 1

# 중간노드를 통해서 대소가 비교되는지
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] & graph[k][j]:
                graph[i][j] = 1 # 방향성 그래프라서 한방향만
                # graph[j][i] = 1 => XX, 플로이드 하면 연결만 되면 방향/대소 무시하고 모든 노드가 연결되니까

print(graph)
answer = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        cnt += graph[i][j] + graph[j][i]
    if cnt == n-1:  # 자기자신 빼고 나머지 노드들과 다 비교했다는 의미
        answer += 1

print(answer)
