from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque([(i,v) for i,v in enumerate(priorities)])

    while True:
        index, prior = q.popleft()
        
        if len(q) == 0:
            answer += 1
            break
            
        if prior < max(q, key=lambda x:x[1])[1] :
            q.append((index, prior))
        else:
            answer += 1
            if index == location :
                break
    
    return answer
