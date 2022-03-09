import math

def is_prime_num(n):
    arr = [True] * (n + 1) # 다 소수라고 가정하고 시작
    arr[0] = False
    arr[1] = False # 소수가 아님

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:    # 이 수가 소수라면, 그 곱들은 다 소수가 아니니까 False 만들기
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1

    return arr

arr = is_prime_num(50)

for i in range(len(arr)):
    if arr[i] == True:
        print(i, end=' ')
