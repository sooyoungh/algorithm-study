# 1) DFS로 풀이
from copy import deepcopy

answer = []
max_diff = 0

# 점수 차이는 다 끝나고 계산


def calcDiff(info, shoot):
    enemyScore, myScore = 0, 0
    for i in range(11):
        if (info[i], shoot[i]) == (0, 0):
            continue
        if info[i] >= shoot[i]:
            enemyScore += (10 - i)
        else:
            myScore += (10 - i)

    return myScore - enemyScore


def dfs(index, arr, n, info): # index로 dfs 깊이 제어!
    global answer, max_diff
    # 답인지 체크
    if index == 11:
        if n != 0:  # n이 남아있는 경우 -> 마지막에 다 주기!
            arr[10] = n
        diff = calcDiff(info, arr)
        result = deepcopy(arr)
        if diff <= 0:
            return
        if max_diff < diff:
            max_diff = diff
            answer = result
        elif max_diff == diff:  # 가장 낮은 점수를 더 많이 맞힌 경우
            for i in range(10, -1, -1):
                
                if result[i] > answer[i]:
                    answer = result
                    break
                elif result[i] < answer[i]:
                    break
                else:   # 두 배열의 i의 갯수가 같으면 continue (코드 생략 가능)
                    continue
        return

    apeach = info[index]  # 어피치 점수

    # 1) 라이언이 질 경우 : 0점
    arr[index] = 0
    dfs(index+1, arr, n, info)

    # 2) 라이언이 이길 경우
    if n - apeach > 0:
        arr[index] = apeach+1
        dfs(index+1, arr, n-(apeach+1), info)


def solution(n, info):

    start_arr = [0]*len(info)
    dfs(0, start_arr, n, info)

    if answer == []:
        return [-1]
    print(answer)
    return answer

