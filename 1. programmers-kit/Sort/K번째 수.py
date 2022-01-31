def solution(array, commands):
    answer = []
    arr = []
    # 행개수 대로 루프
    for n in range(len(commands)):
        i,j,k = commands[n][0], commands[n][1],commands[n][2]
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    
    return answer
