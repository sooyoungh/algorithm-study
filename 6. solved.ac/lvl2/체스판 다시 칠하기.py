import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
