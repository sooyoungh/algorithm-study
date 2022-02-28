n = int(input())
arr = list(map(int, input().split()))

d = [0] * 100
d[0] = arr[0]
d[1] = max(arr[1], d[0])

for i in range(3, n+1):
  d[i] = max(d[i-1], d[i-2] + arr[i])

print(d[n-1])
