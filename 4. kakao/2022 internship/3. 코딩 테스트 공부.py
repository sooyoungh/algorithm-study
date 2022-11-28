def solution(alp, cop, problems):

    goal_al, goal_co = 0, 0
    for p in problems:
        goal_al = max(goal_al, p[0])
        goal_co = max(goal_co, p[1])

    # 목표값보다 이미 클 경우 고려 -> 현재 능력을 목표값으로 설정 (배열 인덱스 범위 초과되지 않도록)
    alp = min(alp, goal_al)
    cop = min(cop, goal_co)

    dp = [[1e9] * (goal_co+1) for _ in range(goal_al+1)]

    dp[alp][cop] = 0

    for i in range(alp, goal_al+1):
        for j in range(cop, goal_co+1):
            if alp == i and cop == j:
                continue
            dp[i][j] = min(dp[i][j], dp[i][j-1] + 1, dp[i-1][j] + 1)

            for al_req, co_req, al_get, co_get, cost in problems:
                if i >= al_req and j >= co_req:
                    new_al = min(i + al_get, goal_al)
                    new_co = min(j + co_get, goal_co)
                    dp[new_al][new_co] = min(
                        dp[new_al][new_co], dp[i][j] + cost)

    return dp[goal_al][goal_co]


# -------------2안)
def solution(alp, cop, problems):

    goal_al, goal_co = 0, 0
    for p in problems:
        goal_al = max(goal_al, p[0])
        goal_co = max(goal_co, p[1])

    # 목표값보다 이미 클 경우 고려 -> 현재 능력을 목표값으로 설정 (배열 인덱스 범위 초과되지 않도록)
    alp = min(alp, goal_al)
    cop = min(cop, goal_co)

    dp = [[1e9] * (goal_co+1) for _ in range(goal_al+1)]

    dp[alp][cop] = 0

    # 1시간씩 공부할 경우
    for i in range(alp, goal_al+1):
        for j in range(cop, goal_co+1):
            if alp == i and cop == j:
                continue
            dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1)

    # 문제 풀어서 시간 더 단축할 수 있는 경우
    for i in range(alp, goal_al+1):
        for j in range(cop, goal_co+1):
            for al_req, co_req, al_get, co_get, cost in problems:
                if i >= al_req and j >= co_req:
                    new_al = min(i + al_get, goal_al)
                    new_co = min(j + co_get, goal_co)
                    dp[new_al][new_co] = min(
                        dp[new_al][new_co], dp[i][j] + cost)

    return dp[goal_al][goal_co]
