import sys
input = sys.stdin.readline

n = int(input())

# 순서대로 새롭게 인덱스 정해주기
data = list(map(int, input().split()))
data_set = set(data)  # 겹치지 않도록
data_list = list(data_set)  # 순서대로

data_list.sort()

data_dict = dict()
for i in range(len(data_list)):
    data_dict[data_list[i]] = i

for i in data:
    print(data_dict[i], end=' ')
