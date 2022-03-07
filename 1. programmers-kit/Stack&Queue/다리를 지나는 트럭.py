from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    sum = 0
    
    while len(truck_weights) > 0:
        answer += 1
        cost = truck_weights[0]
        sum += cost
        
        if len(q) < bridge_length and sum <= weight:
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
