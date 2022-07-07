# 1. 
from itertools import combinations


def solution(relation):
    answer = 0
    n = len(relation)
    col = len(relation[0])
    
    # 키의 모든 조합
    all = set()
    for i in range(1, n+1):
        li = list(combinations(range(col), i))
        all.update(li)

    # 유일성을 만족하는 경우!
    unique = []
    for case in all:  # 키조합 => ex.(학번,이름)
        case_set = set()
        for entity in relation:  # 모든 엔티티 =>  ex.0번째 엔티티 (100,ryan,music,2)
            tmp = []
            for k in case:      # 엔티티를 키조합으로 묶기  => ex.(100,ryan)
                tmp.append(entity[k])
            tmp = tuple(tmp)
            case_set.add(tmp)

        if len(case_set) == n:  # 엔티티 유일성 보장 (해당 키조합으로 모든 엔티티 구분)
            unique.append(case)
    
    
    # 최소성 => (1,2,3)과 (1,2) 있으면 최소만 남기기
    unique.sort() # 정렬 [(0,), (0, 1), (0, 1, 2), (0, 1, 2, 3), (0, 1, 3), (0, 2), (0, 2, 3), (0, 3), (1, 2), (1, 2, 3)]
    answer = set(unique) # {(0, 1), (1, 2), (0, 1, 2), (0, 1, 3), (0, 3), (0, 2, 3), (1, 2, 3), (0, 2), (0, 1, 2, 3), (0,)}
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & (set(unique[j]))):
                answer.discard(unique[j])
    print(answer)

    return len(answer)
