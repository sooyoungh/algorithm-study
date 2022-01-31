# 1. 4자리수 맞춰서 비교
def solution(numbers):
    numbers = [str(x) for x in numbers]
    # 수 대소비교도 문자로 바꿔서
    numbers.sort(key = lambda x : (x*4)[:4], reverse = True)
    if numbers[0] == '0':
        return '0'
    else:
        numbers = ''.join(numbers)
        return numbers

# 2. 두 수 합쳤을 때 큰 거로
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
