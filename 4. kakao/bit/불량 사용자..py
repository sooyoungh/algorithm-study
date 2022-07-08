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
    
# 2. 백트래킹 + 비트마스크
# 순서 상관 있음
# depth로 원소 갯수 제한


# 순서 상관 있음
# depth로 원소 갯수 제한

def solution(user_id, banned_id):
    answer = []
    
    # 아이디 일치 여부 확인
    def possible(user_id, banned_id):
        if len(user_id) != len(banned_id):
            return False
        for uid, bid in zip(user_id, banned_id):
            if bid != '*' and uid != bid:
                return False
        return True

    # 백트래킹 -> depth 체크(id 갯수 제한)
    def backtracking(depth, current):
        nonlocal user_id, banned_id, answer
        if depth == len(banned_id):
            if current in answer:
                return 0
            answer.append(current)
            return 1

        res = 0
        for i in range(len(user_id)):
            if current & (1 << i) or not possible(user_id[i], banned_id[depth]):
                continue
            current |= 1 << i  # 원소 추가
            res += backtracking(depth + 1, current)
            current ^= 1 << i  # 원소 삭제
        return res

    # 시작
    backtracking(0, 0)

    return len(answer)
