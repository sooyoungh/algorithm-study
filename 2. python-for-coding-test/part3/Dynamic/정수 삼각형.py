n = int(input())

data = []
for i in range(n):
  data.append(list(map(int, input().split())))

# 깊은 복사 -> 원래 배열도 값이 변경
# import copy
# arr = copy.deepcopy(data)

# 얕은 복사
# arr = data[:] 혹은 arr = data

arr = [[0 for j in range(i+1)] for i in range(n)]
arr[0][0] = data[0][0]

for i in range(n-1):
  for j in range(i+1):
    pre = arr[i][j]

    left = data[i+1][j] + pre
    right = data[i+1][j+1] + pre

    arr[i+1][j] = max(arr[i+1][j], left)
    arr[i+1][j+1] = max(arr[i+1][j+1], right)

result = max(arr[n-1])
print(result)
