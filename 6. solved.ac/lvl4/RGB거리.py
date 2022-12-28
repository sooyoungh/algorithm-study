import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    data.append(tmp)

tmp = []
min_result = 1e9

# DFS - 시간 초과
def dfs(idx, color_num):
    global min_result
    if idx == n:
        min_result = min(min_result, sum(tmp))
        return
    for i in range(3):
        if color_num == i:  # 색 중복이면 예외!
            continue
        color_val = data[idx][i]
        tmp.append(color_val)
        dfs(idx+1, i)
        tmp.pop()

for i in range(3):
    dfs(0, i)

print(min_result)

# DP
import sys
input = sys.stdin.readline
n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, len(dp)):
    # i번째에 0번 색상 = i-1번째에 0색상 혹은 2번 색상 + i번째에 2번 색상
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

result = min(dp[-1][0], dp[-1][1], dp[-1][2])
print(result)
