n = list(input())

cnt_one = 0
cnt_zero = 0

pre = n[0]
if pre == '0':
  cnt_zero += 1
else:
  cnt_one += 1

for i in range(1, len(n)):
  now = n[i]
  if pre == now:
    continue
  else:
    if now == '1':
      cnt_one += 1
    else:
      cnt_zero += 1


print(min(cnt_one, cnt_zero))
