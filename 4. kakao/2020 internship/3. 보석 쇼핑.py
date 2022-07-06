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
def solution(gems):
    n = len(gems)
    answer = [0, n-1]
    cate = len(set(gems))
    start = 0
    end = 0
    dic = {gems[0]: 1, }  # 지금 담겨있는 딕셔너리

    while start < n and end < n:
        # 모든 종류가 아직 안담긴 경우
        if len(dic) < cate:
            end += 1
            if end == n:
                break
            dic[gems[end]] = dic.get(gems[end], 0) +1  # 없을 경우 1
        else:   # 모든 종류 있는 경우
            
            # 갱신 필요
            length = end - start + 1
            if length < (answer[1] - answer[0] + 1):  
                answer = [start, end]
            
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            
            start += 1

    answer[0] += 1
    answer[1] += 1

    return answer
