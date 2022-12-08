# 이분 탐색
# O(M log(N))
# 10^3 = 2^10
# log(10^3) = log(2^10) => 10정도
n = int(input())
data = list(map(int, input().split()))

m = int(input())
find = list(map(int, input().split()))

data.sort()
for target in find:
    left = 0
    right = n-1
    isExist = False

    while left <= right:
        mid = (left + right)//2
        if target == data[mid]:
            isExist = True
            break
        elif target > data[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if isExist:
        print(1)
    else:
        print(0)
