# 1. BFS - 큐
# 근데 이문제는 모든 결과값을 봐야하고, 
# 인덱스로 접근해야하므로 큐에 넣었다 빼는 것보다 DFS(스택)사용하는 게 더 빠름
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

# 2. BFS - 스택으로 인덱스 접근

def solution(numbers, target):
    idx = 0
    answer = 0
    def dfs(idx, result):
        nonloca answer
        if idx == len(numbers):
            if target == result:
                answer += 1
        else:
            dfs(idx+1, result + numbers[idx])
            dfs(idx+1, result - numbers[idx])
            
    dfs(0,0)
    
    return answer


https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS

