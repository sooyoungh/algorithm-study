# 정석
def solution(N, stages):
    answer = []
    people = len(stages)
    
    for i in range(1, N+1):
        fail_people = stages.count(i)
        if fail_people == 0 or people == 0:
            failure = 0
        else:
            failure = fail_people / people
        answer.append( (i, failure) )
        people -= fail_people
        
    answer.sort( key = lambda x: (-x[1]) )
    
    result = [x[0] for x in answer]
    
    return result
