from itertools import combinations

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


def calc(start, end, tmp):
    tmp_sum = tmp[end-1] - tmp[start]
    return tmp_sum


max_sum = 0
for f_i, f_j, s_i, s_j in combinations(range(m+1), 4):
    max_f = calc(f_i, f_j, first_data)
    max_s = calc(s_i, s_j, second_data)
    tmp_sum = max_f + max_s
    if (max_sum < tmp_sum):
        max_sum = tmp_sum
        print("max_sum")
        print("max_f", max_f)
        print("max_s", max_s)
        print(max_sum)
        print(f_i, f_j, s_i, s_j)
        print()
