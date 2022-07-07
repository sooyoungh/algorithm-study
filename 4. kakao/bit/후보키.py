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


# 2. 비트 마스킹
# 2-1) 엔티티 구분용 - 튜플로
def solution(relation):
    answer = []
    col_n = len(relation[0])
    entity_n = len(relation)
    
    all = list(range(1, 1 << col_n))
    for case in all: #모든 조합에 대한 검사
            tmp_set = set()
            for e in range(entity_n): # entity 마다
                tmp = []
                for col in range(col_n): # col 마다
                    if case & (1<<col):
                        tmp.append(relation[e][col]) # 엔티티 구분용
                tmp = tuple(tmp) # set에는 리스트X 대신 str이나 튜플
                tmp_set.add(tmp)
            
                if len(tmp_set) == entity_n:
                    answer.append(case)
                    
    answer_set = set(answer)
    for i in answer:
        for j in range(i, len(answer)):
            if i & answer[j] == i:
                answer_set.discard(answer[j])
    
    return len(answer_set)

# 2-2) 엔티티 구분용 str
def solution(relation):
    answer = []
    col_n = len(relation[0])
    entity_n = len(relation)
    
    all = list(range(1, 1 << col_n))
    for case in all: #모든 조합에 대한 검사
            tmp_set = set()
            for e in range(entity_n): # entity 마다
                tmp = ""
                for col in range(col_n): # col 마다
                    if case & (1<<col):
                        tmp += str(relation[e][col]) # 엔티티 구분용
                        
                tmp_set.add(tmp)
            
                if len(tmp_set) == entity_n:
                    answer.append(case)
                    
    answer_set = set(answer)
    for i in answer:
        for j in range(i, len(answer)):
            if i & answer[j] == i:
                answer_set.discard(answer[j])
    
    return len(answer_set)

