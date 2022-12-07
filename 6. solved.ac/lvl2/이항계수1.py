from itertools import combinations
n = 5
k = 2

# 0. 조합 라이브러리
print(len(list(combinations(range(n), k))))


# 1. 조합
def fac(n):
    result = 1  # 0! 도 1이니까
    for i in range(2, n+1):
        result *= i
    return result


print(fac(n) // (fac(n-k) * fac(k)))

# 2. 이항계수의 성질 - 재귀


def coef(n, k):
    if n == 0 or n == k:
        return 1
    return coef(n-1, k) + coef(n-1, k-1)


print(coef(n, k))
