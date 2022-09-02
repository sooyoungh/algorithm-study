import sys
input = sys.stdin.readline

n, m = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(n)]

# 0으로 찬 행/열을 추가해주기 위해!
# 원래의 첫 행/열도 똑같은 연산을 위해
dp = [[0]*(m+1) for _ in range(n+1)]

# (i, j)로 도착할때의 최대 캔디갯수는,
# (i, j)의 캔디갯수와   // 이때 candy와 dp의 인덱스 값에 차이 반영해줄것
# (i-1, j), (i, j-1), (i-1, j-1) 중 최대 캔디개수의 합!
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = candy[i-1][j-1] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[n][m])
