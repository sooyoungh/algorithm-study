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
