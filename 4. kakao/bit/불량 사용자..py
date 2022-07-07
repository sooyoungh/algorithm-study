# 1. 순열 -> 반복문 비교
from itertools import permutations

def check(a, ban):
    n = len(a)
    ban_n = len(ban)
    if n != ban_n:
        return False
    for i in range(n):
        if ban[i] == '*':
            continue
        if a[i] != ban[i]:
            return False
    return True

def solution(user_id, banned_id):
    answer = []
    n = len(user_id)
    ban_n = len(banned_id)
    all = list(permutations(user_id, ban_n))

    for tmp in all:
        for i in range(ban_n):  # ('frodo', 'abc123')와 ["fr*d*", "abc1**"] 비교하기
            if not check(tmp[i], banned_id[i]):
                break
            if i == (ban_n-1):
                tmp = set(tmp)
                if not tmp in answer:
                    answer.append(tmp)

    return len(answer)
    
# 2. 비트마스크
