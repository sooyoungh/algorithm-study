# 문자열을 리스트로
s =list(input())
n = []
alpa = 0
result = ''

for i in range(len(s)):
  if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
    n.append(s[i])
  else:
    alpa += int(s[i])

n.sort()

result = ''.join(n)
result = result + str(alpa)

print(result)
