# ---------서브태스크 1만 통과-----------
# 시간 복잡도 통과X
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

# 1. Pn 만들기
p = ["I"]
for i in range(n):
    p.append("OI")
p = "".join(p)

answer = 0
# 2. 문자열 계산해보기
p_len = len(p)
for i in range(0, m-p_len):
    tmp = "".join(s[i:i+p_len])
    if tmp == p:
        answer += 1


print(answer)

# ------------ 시간복잡도 해결 -------------
answer = 0
oi_cnt = 0
i = 0

while i < m-1:
    if s[i:i+3] == "IOI":
        i += 2
        oi_cnt += 1
        if oi_cnt == n:
            answer += 1
            oi_cnt -= 1
    else:
        i += 1
        oi_cnt = 0

print(answer)
