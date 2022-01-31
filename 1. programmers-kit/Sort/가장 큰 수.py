def solution(numbers):
    numbers = [str(x) for x in numbers]
    # 수 대소비교도 문자로 바꿔서
    numbers.sort(key = lambda x : (x*4)[:4], reverse = True)
    if numbers[0] == '0':
        return '0'
    else:
        numbers = ''.join(numbers)
        return numbers
