import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

answer = []


def quad(x, y, n):
    global answer
    start = graph[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if start != graph[i][j]:
                # 해당 영역을 다시 4등분
                answer.append("(")
                quad(x, y, n//2)
                quad(x, y+n//2, n//2)
                quad(x+n//2, y, n//2)
                quad(x+n//2, y+n//2, n//2)
                answer.append(")")
                return
    answer.append(start)


quad(0, 0, n)
result = "".join(map(str, answer))
print(result)
