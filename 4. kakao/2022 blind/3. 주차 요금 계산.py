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
