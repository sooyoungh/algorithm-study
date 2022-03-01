def solution(s):
    answer = len(s)
    n = len(s)
    
    # 얼만큼 자를 수 있는지 단위
    for step in range(1, n//2 +1):
        compress = ""
        cnt = 1
        prev = s[0:step]
        # 파이썬 반복문 -> 증가폭, n만 빼고 가능한 i 돌기!
        for j in range(step,n,step):
            if prev == s[j:j+step]:
                cnt += 1
            else:
                if cnt>= 2:
                    compress += str(cnt) + prev
                else:
                    compress += prev
                prev = s[j:j+step]
                cnt = 1
        if cnt>= 2:
            compress += str(cnt) + prev
        else:
            compress += prev
        answer = min(answer, len(compress))
        
    return answer
