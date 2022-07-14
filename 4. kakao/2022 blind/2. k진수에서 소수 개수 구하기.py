import math

# n을 k진수로 변환하기
def change(n, k):
    result = ""
    while n > 0:
        result += str(n % k)
        n = n // k
    return ''.join(reversed(result))

# 문제) 10진법으로 보았을 때 소수인지 판단


# 소수 체크1) - 모든 숫자 돌면서(오래 걸림)
# def check(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True

# 소수 체크2) - 제곱근까지만 검사(효율적)
# 1과 자기자신을 제외한 약수가 존재하는지 확인하려면, 자기자신의 제곱근(루트)까지만 확인하면 된다.
def check(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):  # 2부터 x의 제곱근까지의 숫자
        if x % i == 0:		# 나머지가 없으면, 즉 나눠떨어지는 숫자가 있으면 소수가 아님
            return False
    return True


def solution(n, k):
    answer = 0
    s = change(n, k)
    for num in s.split('0'):  # '0' 기준 문자열 나누기
        if not num:
            continue
        if check(int(num)):
            answer += 1
    return answer
