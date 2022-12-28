import sys
input = sys.stdin.readline

tc = int(input())


def solution():
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(2)]

    # data[a][b] : a번째 줄에 b 인덱스 값까지 포함할때의 최대값
    for i in range(1, n):
        if i == 1:
            data[0][i] += data[1][i-1]
            data[1][i] += data[0][i-1]
        else:
            # 1. 위아래 지그재그
            # 2. 중간에 한 칸 쉬고 지그재그 가는 방법
            data[0][i] += max(data[1][i-1], data[1][i-2])
            data[1][i] += max(data[0][i-1], data[0][i-2])
    print(max(data[0][-1], data[1][-1]))


for i in range(tc):
    solution()
