import math
from itertools import permutations

# 소수 찾기

# 약수의 특성을 생각해보면
# 1과 자기자신 제외하고 곱해진 수가 있는 지 찾아볼때
# 제곱근까지만 찾아보면 됨!
# 왜냐면 약수에서 제곱근 기준으로 작은수-큰수가 대칭되므로

def check (n):
    if n == 1: # 1은 소수 아님
        return False
    for i in range(2, int(math.sqrt(n))+ 1): 
        if n % i == 0: 
            return False
    return True

def solution(numbers):
    # 중복이 안들어가는 set 사용!
    answer = set()
    data = list(numbers)
    # 문자열을 배열로 바꾸려면 list() // 반대는 arr = str.split()
    
    for j in range(1, len(data)+1):
        for i in permutations(data, j):
            # 배열종류를 -> 문자열로 합치기
            tmp = ''.join(i)
            if tmp[0] == '0':
                continue
            if check(int(tmp)):
                answer.add(tmp)
    
    return len(answer)
