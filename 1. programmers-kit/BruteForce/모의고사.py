def solution(answers):
    result = []
    fir = [1, 2, 3, 4, 5]
    sec = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt = [0]*3
    
    for i in range(len(answers)):
        i1 = i%len(fir)
        i2 = i%len(sec)
        i3 = i%len(thr)
        
        if fir[i1] == answers[i]:
            cnt[0] += 1
        if sec[i2] == answers[i]:
            cnt[1] += 1
        if thr[i3] == answers[i]:
            cnt[2] += 1
            
    k = max(cnt)
    for i, v in enumerate(cnt):
        if v == k:
            result.append(i+1)
    
    return result
