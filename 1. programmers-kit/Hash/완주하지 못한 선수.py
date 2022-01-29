def solution(participant, completion):
    answer = ""
    result = dict()
    length = len(participant)
    
    # participant을 해시로 (해시에 값이 있는지 먼저 판단, 동명이인)
    for i in participant:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
            
    for j in completion:
        result[j] -= 1
        
    for i in range(length):
        if result[participant[i]] > 0:
            return participant[i]
