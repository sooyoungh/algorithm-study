def solution(citations):
    citations.sort()
    
    # h 찾기
    for i in range(len(citations)):
        if citations[i] >= (len(citations)-i):
            h = len(citations)-i
            break
    
    return h
