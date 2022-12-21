from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = defaultdict(int)


def calc(x, y, size):
    num = graph[x][y]
    flag = True  # 다 같은 지
    for i in range(x, x+size):
        for j in range(y, y+size):
            if graph[i][j] != num:
                flag = False
                break
        if not flag:
            break

    if flag:  # 9개 모든 데이터가 같은 값이면
        result[num] += 1
        return

    # 9개가 같은 값이 아니므로 나누기 진행
    new_size = size // 3
    for i in range(3):
        for j in range(3):
            calc(x + i*new_size, y + j*new_size, new_size)


calc(0, 0, n)

print(result[-1])
print(result[0])
print(result[1])
