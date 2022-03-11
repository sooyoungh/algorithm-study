# 총 전체 시간을 total이라 가정하고 이분탐색
def solution(n, times):
    answer = 0
    start, end = 1, max(times)*n

    while start < end:
        mid = (start + end) // 2
        total = 0
        for time in times:
          # total 시간내에 각 심사원들이 몇명을 받을 수 있는지?
            total += mid // time
            
        # n명 받을수 있으면 시간 더 줄여보기
        if total >= n:
            end = mid
        else: # n명 못받으면 시간 늘이기
            start = mid + 1
            
    answer = start
    return answer
