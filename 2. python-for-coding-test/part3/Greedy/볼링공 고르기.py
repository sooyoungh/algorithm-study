n, m = map(int, input().split())
arr = list(map(int, input().split()))

data = [0]*(m+1)
for i in range(len(arr)):
  data[arr[i]] += 1

cnt = 0
for i in range(len(data)):
  if data[i] == 0 or data[i] == 1:
    continue
  elif data[i] == 2:
    cnt += 1
  else:
    num = data[i]
    cnt += (num*(num-1))//2

answer = (n*(n-1)) //2 - cnt

print(answer)
