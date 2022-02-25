n = int(input())
data = []
for i in range(n):
  t,p = map(int, input().split())
  data.append((t,p))
max_value = 0
print(data)
dp = [0] * (n)

for i in range(n-1, -1, -1):
  time, pay = data[i]
  if (i + time) <= n:
    dp[i] = max( pay + dp[i + time], max_value)
    max_value = dp[i]
  else:
    dp[i] = max_value

print(dp[0])
