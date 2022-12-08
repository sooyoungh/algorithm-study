import sys
input = sys.stdin.readline

n, k = map(int, input().split())

data = [i for i in range(1, n+1)]
answer = []

index = 0
for i in range(n):
    index += (k-1)
    if index >= len(data):
        index = index % len(data)

    tmp = data.pop(index)
    answer.append(str(tmp))
print("<" + ", ".join(answer) + ">")

# 리스트.pop(인덱스번호) : 해당 인덱스의 데이터 삭제 후 리턴
# 리스트.pop() : 가장 마지막 인덱스 삭제 후 리턴
# 리스트.remove(데이터) : 해당 데이터 삭제
# 리스트.remove() : 가장 첫번째 데이터 삭제
# del 리스트[인덱스] : 해당 요소 삭제

# https://www.delftstack.com/ko/howto/python/what-is-difference-between-del-remove-and-pop-on-python-lists/
