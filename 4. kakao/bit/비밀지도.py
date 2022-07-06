# 비트마스킹
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):                    # bin() => 이진수(binary) 문자열로
        tmp = bin(arr1[i] | arr2[i])[2:]  # 0b11111 이면 0b를 제거하기 위해
        str = ''
        for j in tmp:
            if int(j) == 1:
                str += "#"
            else:
                str += " "
        if len(str) < n:
            str = " " * (n-len(str)) + str

        answer.append(str)

    return answer
