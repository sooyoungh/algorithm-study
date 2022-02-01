# 튜플에서의 sort 활용
n = int(input())

students = []
for _ in range(len(students)):
  students.append(input().split())

students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]),  int(x[0])) )

for i in students:
  print(i[0])
