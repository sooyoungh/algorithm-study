from collections import defaultdict
import math


def solution(fees, records):
    answer = []
    basic_time = fees[0]
    basic_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    car_inout = defaultdict(list)  # 자동차별 모든 입/출차 기록
    car_time = defaultdict(int) # 자동차별 실제 시간

    def get_second(time):
        h, m = map(int, time.split(':'))
        all = (h * 60) + m
        return all

    for i in range(len(records)):
        time, car, data = records[i].split()
        car_inout[car].append((time, data))

    car_time = list(car_inout.keys())
    car_time.sort()
    n = len(car_time)
    answer = [0] * n
    i = 0

    # 각 자동차별 시간 체크
    for case in car_time:
        all_time = 0
        # '0000': [('06:00', 'IN'), ('06:34', 'OUT'), ('18:59', 'IN')]
        for time, data in car_inout[case]:
            if data == "IN":
                in_time = get_second(time)
            else:
                out_time = get_second(time)
                all_time += out_time - in_time
                in_time = -1
        # 마지막이 IN일 경우 체크
        if in_time != -1:
            all_time += get_second("23:59") - in_time
        answer[i] = all_time
        i += 1

    # 가격 계산
    new_answer = []

    for case in answer:
        if case <= basic_time:
            new_answer.append(basic_fee)
        else:
            new_fee = basic_fee
            new_fee += math.ceil((case - basic_time) / unit_time) * unit_fee
            new_answer.append(new_fee)
    print(new_answer)

    return new_answer


# ------------------------시간 
from collections import defaultdict
from collections import deque
import math


def solution(fees, records):
    answer = []
    basic_time = fees[0]
    basic_money = fees[1]
    plus_time = fees[2]
    plus_money = fees[3]

    data = defaultdict(list)
    time_cnt = defaultdict(int)  # 각 차량별 시간
    money = defaultdict(int)  # 각 차량별 돈

    # 1. 차 정보 입력
    for tmp in records:
        time, car, in_out = tmp.split()
        car = int(car)
        hour, min = time.split(':')
        time = (int(hour)*60) + int(min)
        data[car].append((time, in_out))
    print(data)

    # 딕셔너리를 키로 정렬하기 위해 key값만 정렬
    sorted_keys = sorted(data.keys())

    # 2. 차량별 시간 계산
    for key in sorted_keys:
        total_time = 0
        q = deque()

        for time, in_out in data[key]:
            if in_out == 'IN':
                q.append(time)
            elif in_out == 'OUT':
                in_time = q.popleft()
                out_time = time
                total_time += out_time - in_time

        if len(q) != 0:  # 출차 안하면, 23:59로 계산
            print("혹시..")
            in_time = q.popleft()
            total_time += ((23 * 60) + 59) - in_time
        time_cnt[key] = total_time

    # 3. 차량별 돈 계산
    for car, time in time_cnt.items():
        if time <= basic_time:
            money[car] = basic_money
        else:
            tmp_time = math.ceil((time - basic_time) / plus_time)
            money[car] = basic_money + tmp_time * plus_money

    return money


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))
