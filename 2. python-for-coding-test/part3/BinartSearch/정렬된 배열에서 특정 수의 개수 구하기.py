n, x = map(int, input().split())
data = list(map(int, input().split()))

def find_first(data, x):
  start = 0
  end = len(data)-1
  while start < end:
    mid = (start + end)//2
    if data[mid] == x :
      if data[mid - 1] < x:
        return mid
      else:
        end = mid
    elif data[mid] > x :
      end = mid - 1
    else:#
      start = mid + 1
  return -1

def find_last(data, x):
  start = 0
  end = len(data)-1
  while start < end:
    mid = (start + end)//2
    if data[mid] == x :
      if data[mid + 1] > x:
        return mid
      else:
        start = mid
    elif data[mid] > x :
      end = mid - 1
    else:
      start = mid + 1
  return  -1


first = find_first(data, x)
last = find_last(data, x)

if first == -1:
  print(-1)
else:
  print(last - first + 1)
