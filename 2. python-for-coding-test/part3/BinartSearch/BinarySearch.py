
# 이진탐색 - 재귀함수-> 끝나는 시점을 정해줘야
def binary_search(arr, target, start, end):
  if start > end:
    return None
  mid = (start + end)//2
  if arr[mid] == target:
    return mid
  elif arr[mid] > target:
    return binary_search(arr, target, start, mid - 1)
  else:
    return binary_search(arr, target, mid +1, end)

# 이진탐색 - 반복문
def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start + end)//2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None
