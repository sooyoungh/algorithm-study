import sys
input = sys.stdin.readline

# 최소 => '-' 기준으로 괄호치기
# + 부분은 더해주기
nums_list = input().split('-')
data = []

for dummy in nums_list:
    tmp_sum = 0
    for tmp in dummy.split('+'):
        tmp_sum += int(tmp)
    data.append(tmp_sum)

answer = data[0]
n = len(data)
for i in range(1, n):
    answer -= data[i]
print(answer)
