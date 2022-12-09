from math import factorial
import sys
input = sys.stdin.readline


# 1) 직접 구해주기
n = int(input())
zero_cnt = 0
calc = str(factorial(n))
for i in calc[::-1]:
    if i != 0:
        break
    zero_cnt += 1

print(zero_cnt)


# 2) 5의 개수 세기
# 10 = 2 * 5
# 2, 5가 곱해진 횟수 중 작은 값이 10이 곱해진 횟수
# 5가 더 적게 곱해지므로 5의 횟수를 구하면 된다!
n = int(input())
cnt = 0

while n >= 5:
    cnt += n // 5  # 5가 곱해진 갯수 => 0의 갯수
    n //= 5  # 25가 곱해진 경우, 갯수 한번씩 더 세기

print(cnt)
