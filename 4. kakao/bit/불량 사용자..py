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

def solution(user_id, banned_id):
    answer = []
    backtracking(0, user_id, banned_id, 0, answer)
    return len(answer)


def backtracking(depth, user_ids, banned_ids, current, ans):
    if depth == len(banned_ids):
        if current in ans:
            return 0
        ans.append(current)
        return 1

    res = 0
    for i in range(len(user_ids)):
        if current & (1 << i) or not possible(user_ids[i], banned_ids[depth]):
            continue
        current |= 1 << i  # 원소 추가
        res += backtracking(depth + 1, user_ids, banned_ids, current, ans)
        current ^= 1 << i  # 원소 삭제
    return res


def possible(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    for uid, bid in zip(user_id, banned_id):
        if bid != '*' and uid != bid:
            return False
    return True
