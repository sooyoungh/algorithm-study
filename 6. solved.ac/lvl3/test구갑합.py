
def getMaxInRange(start, end, tmp):
    # 이 구간에서의 최대 합 찾기!
    max_sum = tmp[start]
    for i in range(start, end):
        for j in range(start+1, end+1):
            tmp_sum = tmp[j] - tmp[i]
            max_sum = max(max_sum, tmp_sum)
    return max_sum


tmp = [1, 2, -3, 4, 5]
tmp_sum = [1, 2, -3, 4, 5]
for i in range(1, 5):
    tmp_sum[i] += tmp_sum[i-1]
print(tmp_sum)
result = getMaxInRange(0, 4, tmp_sum)
print(result)
