# 1. 누적합

# 초로 환산하기
def get_seconds(time):
    h, m, s = map(int, time.split(":"))
    return (h*60*60) + (m*60) + s

# 시간을 문자열로
def time_to_str(time):
    h = time // (60**2)
    h = '0' + str(h) if h < 10 else str(h)
    time %= 60**2

    m = time // (60)
    m = '0' + str(m) if m < 10 else str(m)

    time %= 60
    s = '0' + str(time) if time < 10 else str(time)
    
    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):  
    play_time = get_seconds(play_time)
    adv_time = get_seconds(adv_time)
    times = [0] * (play_time + 1)
    
    # 1. 시작/종료시간 기록
    for log in logs:
        start, end = log.split('-')
        start = get_seconds(start)
        end = get_seconds(end)
        # 시작, 종료지점 표시
        times[start] += 1
        times[end] -= 1

    # 2. 구간별 시청 기록 (+1 부터 -1까지)
    for i in range(1, play_time):
        times[i] += times[i-1]
    
    # 3. 누적 시청 기록
    for i in range(1, play_time):
        times[i] += times[i-1]

    max_value = -1
    answer = 0
    
    # 4. DP 배열을 이용한 누적합 구하기 : times[i] - times[i - adv_time]
    # i : 끝점, answer : 시작점
    # 끝점 기준으로 반복문
    for i in range(adv_time-1, play_time):
        tmp = times[i] - times[i-adv_time] 
        if tmp > max_value:
            max_value = tmp
            answer = i - adv_time + 1

    return time_to_str(answer)
