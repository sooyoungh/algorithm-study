n = 10
first_data = list(map(int, input().split()))
second_data = list(map(int, input().split()))

m = len(first_data)

# 1. 누적합 세팅하기
for i in range(1, m):
    first_data[i] += first_data[i-1]
    second_data[i] += second_data[i-1]

print(first_data)
print(second_data)


def getMaxInRange(start, end, tmp):
    # 이 구간에서의 최대 합 찾기!
    max_sum = tmp[start]
    for i in range(start, end):
        for j in range(start+1, end+1):
            tmp_sum = tmp[j] - tmp[i]
            if (tmp_sum > max_sum):
                max_sum = tmp_sum
                print("here", i, j, max_sum, tmp)
    return max_sum


for i in range(1, n-1):
    # first_len = j-i-1
    # second_len = m-j
    max_first_second = 0
    fisrt_max = getMaxInRange(0, i-1, first_data)
    second_max = getMaxInRange(i, m-1, second_data)
    tmp_f_s = fisrt_max + second_max
    if tmp_f_s > max_first_second:
        max_first_second = tmp_f_s
        print("index : ", i)

print(fisrt_max)
print(second_max)
print(max_first_second)
# print(cases)
# 3. 각각 게산하기
