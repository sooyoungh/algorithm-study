# 1. 시간 초과
def solution(gems):
    answer = []
    total = len(gems)
    arr = set(gems)
    size = len(arr)

    for n in range(size, total):
        for start in range(total-n+1):
            new_arr = gems[start:start+n]
            flag = True
            # 하나라도 없으면 False
            for i in arr:
                if not i in new_arr:
                    flag = False
            if flag == True:
                answer = [start+1, start+n]
                return answer

    answer = [1, total]
    return answer

# 2. 투 포인터 알고리즘
