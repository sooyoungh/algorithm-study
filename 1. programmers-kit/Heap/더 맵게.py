import heapq

def solution(scoville, K):
    q = []
    heapq.heapify(scoville)
    cnt = 0
    
    
    while scoville[0] < K:
        # 제한 조건 놓치지 말기
        if len(scoville) == 1:
            return -1
        cnt += 1
        fir = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
    
        after = fir + (sec*2)
        heapq.heappush(scoville, after)
        
    
    return cnt
