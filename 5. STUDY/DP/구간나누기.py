import sys
input = sys.stdin.readline

n, m = map(int, input().split())
MIN = -1e9
case1 = [[0]+[MIN]*m for _ in range(n+1)]  # 앞 원소 제외, 앞 n-1개의 최대 구간합
case2 = [[0]+[MIN]*m for _ in range(n+1)]  # 앞 원소 포함, 앞 n개의 최대 구간합

for i in range(1, n+1):
    tmp = int(input())
    for j in range(1, min(m, (i+1)//2)+1):
        # 앞 원소 제외, 앞 n-1개의 최대 구간합
        case1[i][j] = max(case1[i-1][j], case2[i-1][j-1]) + tmp
        # 앞 원소 포함, 앞 n개의 최대 구간합
        case2[i][j] = max(case1[i-1][j], case2[i-1][j])

print(max(case1[-1][-1], case2[-1][-1]))
