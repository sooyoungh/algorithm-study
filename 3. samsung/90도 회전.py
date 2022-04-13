def rotate(graph):
    n = len(graph)
    result = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            result[y][n-1-x] = graph[x][y]
    return result
