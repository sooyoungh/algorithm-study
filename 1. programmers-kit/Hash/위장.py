def solution(clothes):
    # 항목별 개수를 딕셔너리로
    data = dict()
    
    for i in range(len(clothes)):
        name = clothes[i][1]
        data[name] = data.get(name, 0) + 1

    answer = 1
    for k,v in data.items():
        answer *= (v+1) # 해당을 의상을 안입은 경우도 포함

    answer-= 1
        
    return answer
