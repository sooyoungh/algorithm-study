# 참고) 파이썬 매개변수의 주소값 => id(arr)로 체크해보기

from copy import deepcopy

answer = []
max_diff = 0


def calc_diff(enemy, my):
    enemy_score, my_score = 0, 0
    for i in range(11):
        if (enemy[i], my[i]) == (0, 0):
            continue
        elif enemy[i] >= my[i]:
            enemy_score += (10 - i)
        else:
            my_score += (10 - i)
    return my_score - enemy_score


def dfs(round_num, my, shoot_left, enemy):
    global answer, max_diff

    # 마지막 라운드일 경우
    if round_num == 11:
        if shoot_left != 0:  # shoot 갯수가 남아있으면, 마지막 점수 몰빵
            my[10] = shoot_left
        tmp_diff = calc_diff(enemy, my)  # 점수차 계산

        if tmp_diff <= 0:  # 내가 지면 패스
            return
        elif max_diff < tmp_diff:  # 이번이 점수차가 더 크면 결과 업데이트
            max_diff = tmp_diff
            answer = deepcopy(my)
        elif max_diff == tmp_diff:  # 점수차 같으면 낮은 점수 더 많이 맞힌 경우
            for i in range(10, -1, -1):
                if my[i] > answer[i]:
                    answer = deepcopy(my)  # 현재 껄로 업데이트
                    break
                elif my[i] < answer[i]:  # 업데이트 안함
                    break
        return

    # 라운드 진행

    # 1) 이번 라운드에서 내가 지는 경우
    my[round_num] = 0  # 질때는 0으로
    dfs(round_num+1, my, shoot_left, enemy)

    # 2) 이번 라운드에서 내가 이기는 경우
    if shoot_left > enemy[round_num]:
        my[round_num] = enemy[round_num] + 1
        dfs(round_num+1, my, shoot_left - (enemy[round_num] + 1), enemy)


def solution(n, info):
    my = [0] * len(info)
    dfs(0, my, n, info)

    if answer == []:
        return [-1]
    return answer


n = 5
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
print(solution(n, info))
