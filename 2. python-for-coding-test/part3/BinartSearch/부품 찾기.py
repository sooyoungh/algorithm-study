# 1. 이진 탐색
n = int(input())
data = list(map(int, input().split()))
m = int(input())
find_data = list(map(int, input().split()))

data.sort()

for i in range(len(find_data)):
  target = find_data[i]
  start = 0
  end = len(data)
  while start <= end:
    mid = (start+end)//2
    if data[mid] == target:
      print("yes", end=' ')
      break
    elif data[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  if data[mid] != target:
    print("no", end=' ')
