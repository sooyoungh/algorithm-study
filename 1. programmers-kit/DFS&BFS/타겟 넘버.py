from collections import deque

def solution(numbers, target):
    queue = deque([])
    answer = 0
    
    queue.append((numbers[0], 0))
    queue.append((-1 * numbers[0], 0))
    
    while queue:
        now, idx = queue.popleft()
        idx += 1
        if idx < len(numbers):
            queue.append((now + numbers[idx], idx))
            queue.append((now + (-1 * numbers[idx]), idx))
        else:
            if target == now:
                answer += 1
            
    return answer


# 왜 큐를 사용하는지

https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS
