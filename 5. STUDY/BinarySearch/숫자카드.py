import sys
input = sys.stdin.readline


# 숫자 카드
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))


cards.sort()


def binary_search(target, start, end):
    while start <= end:
        mid = (start + end)//2

        if cards[mid] == target:
            return mid
        elif cards[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(data[i], 0, n-1) != None:
        print(1, end=' ')
    else:
        print(0, end=' ')
