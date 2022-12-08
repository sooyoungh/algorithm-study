n = int(input())
data = list(map(int, input().split()))

# 약수들은 자기자신의 제곱근 기준으로 대칭적으로 존재하기에,
# 자신의 제곱근까지의 수만 확인하면 된다.


def find(num):
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False

    return True


answer = 0
for i in data:
    if i == 1:
        continue
    if (find(i)):
        answer += 1

print(answer)
