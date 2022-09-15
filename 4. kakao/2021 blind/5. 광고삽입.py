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

# 2. 투포인터 -> 다시!!
def s2i(s):
    z = s.split(':')
    return int(z[0])*3600+int(z[1])*60+int(z[2])

def i2s(t):
    ret = ''
    ret += str(t//3600).zfill(2)+':'
    t %= 3600
    ret += str(t//60).zfill(2)+':'
    t %= 60
    ret += str(t).zfill(2)
    return ret

def solution(play_time, adv_time, logs):
    event = []
    pt, at = s2i(play_time), s2i(adv_time)
    
    # A. 전처리
    for l in logs:
        st,en = map(s2i, l.split('-'))
        event.append((st,1))
        event.append((en,-1))
    event.append((0, 0));
    event.sort()
    
    # B. 누적 재생시간이 가장 많은 곳 계산
    # cnt1 : 시작 구간에서의 시청중인 사람의 수
    # cnt2 : 끝 구간에서의 시청중인 사람의 수
    idx1, idx2, cnt1, cnt2 = 0, 0, 0, 0
    curtime, curval = 0, 0
    while idx2 < len(event) - 1 and event[idx2+1][0] <= at:
        curval += (event[idx2+1][0]-event[idx2][0]) * cnt2
        cnt2 += event[idx2+1][1]
        idx2 += 1
    curval += (at - event[idx2][0]) * cnt2
    mxval = curval
    mxtime = 0
    while curtime <= pt-at and idx2 < len(event) - 1:
        delta1 = event[idx1+1][0] - curtime
        delta2 = event[idx2+1][0] - (curtime + at)
        if delta1 <= delta2: # 시작 구간이 다음 event에 더 가까운 경우
            curval = curval + (cnt2 - cnt1) * delta1
            cnt1 += event[idx1+1][1]
            idx1 += 1
            curtime += delta1
        else:
            curval = curval + (cnt2 - cnt1) * delta2
            cnt2 += event[idx2+1][1]
            idx2 += 1
            curtime += delta2
        if curval > mxval:
            mxval, mxtime = curval, curtime
    return i2s(mxtime)


# Reference
# https://blog.encrypted.gg/995
