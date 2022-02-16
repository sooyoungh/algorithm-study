def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return x

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a <b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

edges = [] # (cost, a, b)으로 넣는 리스트임
result = 0

# 부모 테이블 초기화
for i in range(1, v+1):
  parent[i] = i

for _ in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

# 비용 순서대로 정렬 -> 리스트의 원소가 튜플일 경우
edges.sort()

for edge in  edges:
  cost, a,b = edge
  # 사이클 아닐 경우에만 union하기!
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)
