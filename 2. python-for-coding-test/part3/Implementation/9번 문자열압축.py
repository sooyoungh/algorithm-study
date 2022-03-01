def solution(s):
    answer = len(s)
    n = len(s)
    
    # 얼만큼 자를 수 있는지 단위
    for step in range(1, n//2 +1):
        compress = ""
        cnt = 1
        prev = s[0:step]
        # 파이썬 반복문 -> 증가폭, 
        # n-step만큼 전까지만 가능!
        for k in range(step, n, step):
            if prev == s[k:k+step]:
                cnt += 1
            else:
                if cnt>= 2:
                    compress += str(cnt) + prev
                else:
                    compress += prev
                prev = s[k:k+step]
                # k부터 k+step까지 (인덱스랑 달리 슬라이싱은 끝보다 큰 값이어도 가능, 그냥 마지막까지 출력됨!)
                print(k,k+step, end= ' ')
                print()
                cnt = 1
                
        # prev는 무조건 마지막까지 남은 문자열!
        print(prev)
        
        # 남은 문자열 처리
        if cnt>= 2:
            compress += str(cnt) + prev
        else:
            compress += prev
        
        answer = min(answer, len(compress))
        
        
        
    return answer
