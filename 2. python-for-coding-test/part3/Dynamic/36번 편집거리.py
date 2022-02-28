from collections import deque
a_q = deque()
b_q = deque()

a = input()
b = input()

cnt = 0

for i in range(len(a)):
  same = False
  for j in range(len(b)):
    a_alpa = a[i]
    b_alpa = b[j]
    if a_alpa == b_alpa:
      cnt += 1
      break
      
max_len = max(len(a), len(b))
print(max_len - cnt)
