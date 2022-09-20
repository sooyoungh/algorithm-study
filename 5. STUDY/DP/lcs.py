# 1) 2차원 DP
import sys
input = sys.stdin.inputline

# 2차원 DP의 시작을 0 으로 하려고 '1', '2'을 붙여줌!
first = '1' + input().strip()
sec = '2' + input().strip()

n, m = len(first), len(sec)

data = [[0]*(m) for _ in range(n)]

for i in range(n):
    for j in range(m):
        # 같은 문자일 경우,
        # 전의 값 +1
        if first[i] == sec[j]:
            data[i][j] = data[i-1][j-1] + 1
        # 다른 문자일 경우,
        # 한 문자만 덜 비교했을때(위,왼쪽)의 최대값
        else:
            data[i][j] = max(data[i][j-1], data[i-1][j])

print(data[-1][-1])


# 2) 1차원 DP
import sys
input = sys.stdin.readline

first = input().strip()
sec = input().strip()

n, m = len(first), len(sec)

data = [0] * m

for i in range(n):
    same = 0
    # print(first[i], end=' ')
    for j in range(m):
        if same < data[j]:
            same = data[j]
        elif first[i] == sec[j]:
            data[j] = same + 1
    # print(data)

print(max(data))
# print(data)
