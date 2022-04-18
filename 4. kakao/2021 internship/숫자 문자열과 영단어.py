# 1. 딕셔너리 활용
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

# 2. 숫자 -> 배열 활용
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)

# 3.
def solution(s):
    answer = ""
    length = len(s)
    pass_cnt = 0
    
    for i in range(length):
        if pass_cnt > 0:
            pass_cnt -= pass_cnt
            continue
        
        if ord('0') <= ord(s[i]) <= ord('9'):
            answer += s[i]
        else:
            if s[i:i+4] == "zero":
                answer += '0'
                pass_cnt = 4
            elif s[i:i+3] == "one":
                answer += '1'
                pass_cnt = 4
            elif s[i:i+3] == "two":
                answer += '2'
                pass_cnt = 3
            elif s[i:i+5] == "three":
                answer += '3'
                pass_cnt = 5
            elif s[i:i+4] == "four":
                answer += '4'
                pass_cnt = 4
            elif s[i:i+4] == "five":
                answer += '5'
                pass_cnt = 4
            elif s[i:i+3] == "six":
                answer += '6'
                pass_cnt = 3
            elif s[i:i+5] == "seven":
                answer += '7'
                pass_cnt = 5
            elif s[i:i+5] == "eight":
                answer += '8'
                pass_cnt = 5
            elif s[i:i+4] == "nine":
                answer += '9'
                pass_cnt = 4
        
    
    return int(answer)
