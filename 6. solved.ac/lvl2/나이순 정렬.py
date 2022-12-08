import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    age, name = input().split()
    data.append((int(age), name))

# 정렬기준 2) 들어온 순서대로 이미 정렬되어 있음

# 정렬기준 1) 다음으로 나이순 정렬
# (정렬 우선순서와 실제 정렬해주는 순서를 반대로 해야함)
data.sort(key=lambda x: (x[0]))

for i in data:
    age, name = i
    print(age, end=' ')
    print(name)
