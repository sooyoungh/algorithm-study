import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())

data = []
for i in range(n):
    data.append(int(input()))

# 데이터가 100만 까지 입력가능
# O(logN)

data.sort()
for i in data:
    print(i)

# 정렬 알고리즘 추가 ++
