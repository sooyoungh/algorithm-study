# 1. 내풀이 - 그냥 자료구조 2개
n,m = map(int, input().split())
edges = []
for i in range(m):
  a,b = map(int, input().split())
  edges.append((a,b))
  
parent_list = [[] for i in range(n+1)]
child_list = [[] for i in range(n+1)]

for i in range(1,n+1):
  parent_list[i].append(i)
  child_list[i].append(i)
  
# edge 별로 자식, 부모 줄줄이 연결
for edge in edges:
  child, parent = edge
  parent_list[child].append(parent)
  child_list[parent].append(child)
  
  for i in parent_list[parent]:
    if i == parent:
      continue
    # 기존 부모 리스트랑도 겹치지 않아야함
    # 기존 부모 리스트 돌았을 때 겹칠 경우 flag = False, 이 경우 새로 저장 안함!
    flag = True
    for k in parent_list[child]:
      if i == k:
        flag = False
        break
    if flag:
      parent_list[child].append(i)
    
  for j in child_list[child]:
    if j == child:
      continue
    flag = True
    for k in child_list[parent]:
      if j ==k:
        flag = False
        break
    if flag:
      child_list[parent].append(j)

print(parent_list)
print(child_list)

result = 0
for i in range(1, n+1):
  cnt_child = len(child_list[i])
  cnt_parent = len(parent_list[i])
  print(i, cnt_parent, cnt_child)
  if cnt_child + cnt_parent -2 == (n-1):
    result += 1

print(result)
