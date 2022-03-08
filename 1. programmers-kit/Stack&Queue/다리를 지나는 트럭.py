
# 스택을 접근하는 거랑 pop하는 거랑 다른 점을 이용
# 주의: 큐에서 빼낼때는 len(q) > 0 이어야 함!

# 1. 내풀이 - 구현처럼
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    sum = 0
    
    while len(truck_weights) > 0:
        answer += 1
        # 스택 값 접근
        cost = truck_weights[0]
        sum += cost
        
        if len(q) < bridge_length and sum <= weight:
            # 스택값 pop
            now = truck_weights.pop(0)
            q.append([now,0])
            print(q)
        else:
            sum -= cost
            
        # 도로 위에 있는 차들 시간 +1
        for i in range(len(q)):
            q[i][1] += 1
                
        # 도로에서 시간 다 되서 빠질 수 있으면 빼기
        if len(q) > 0:
            if q[0][1] == bridge_length:
                sum -= q[0][0]
                q.popleft()
            
    
    return answer+bridge_length


# 2. sum함수가 오래 걸려서 변수로 만들고, 뺴고 더하기
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length
    sum = 0
    while q:
        time += 1
        sum -= q.pop(0)
        
        if truck_weights:
            if sum + truck_weights[0] <= weight:
                cost = truck_weights.pop(0)
                q.append(cost)
                sum += cost
            else:
                q.append(0)
    
    return time
