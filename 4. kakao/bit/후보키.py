# 1. set, 리스트만으로
from itertools import combinations


def solution(relation):
    col_n = len(relation[0])
    entity_n = len(relation)

    all = []
    for n in range(1, col_n+1):
        for tmp in combinations(range(col_n), n):
            all.append(tmp)

    # 유일성
    answer = []
    for case in all:
        tmp_set = set()
        for entity in relation:
            tmp = []
            for i in case:
                tmp.append(entity[i])
            tmp = tuple(tmp)
            tmp_set.add(tmp) # tmp_set에 중복은 한번만 더해짐
        if len(tmp_set) == entity_n:
            answer.append(case)

    # 최소성
    new_answer = set(answer)
    for i in range(len(answer)):
        for j in range(i+1, len(answer)):
            if len(answer[i]) == len( set(answer[i]) & set(answer[j])):
                new_answer.discard(answer[j])

    return len(new_answer)


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

