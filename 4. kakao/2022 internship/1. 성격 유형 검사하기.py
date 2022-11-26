from collections import defaultdict


def solution(survey, choices):
    answer = ''
    types = [
        ['R', 'T'],
        ['C', 'F'],
        ['J', 'M'],
        ['A', 'N'],
    ]

    result = defaultdict(int)

    # 항목별 점수 계산
    for type, point in zip(survey, choices):
        if point < 4:
            user_type = type[0]
            result[user_type] += 4 - point
        elif point > 4:
            user_type = type[1]
            result[user_type] += point - 4

    # 최종 타입 결정
    for i in types:
        type_one = i[0]
        type_two = i[1]
        if result[type_one] >= result[type_two]:
            answer += type_one
        else:
            answer += type_two

    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

print(solution(survey, choices))
