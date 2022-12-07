import math
n, m = map(int, input().split())

# ------------1. 직접-------------
# 최대 공약수
for i in range(min(n, m), 0, -1):
    if n % i == 0 and m % i == 0:  # 둘다 나누어 떨어지는 수 (공약수) 중 최대
        print(i)
        break

# 최소 공배수
for i in range(max(n, m), n * m + 1):
    if i % n == 0 and i % m == 0:
        print(i)
        break

# ------2. 유클리드 호제법------------


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


# ------3. 유클리드 호제법 - 공식------
print(math.lcm(n, m))
print(math.gcd(n, m))


# -------번외) 약수
def get(n):
    arr = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            arr.append(i)
            # 짝이 되는 약수도 구할 경우
            if ((i**2) != n):  # 자신의 제곱근은 2번 세지 않도록!
                arr.append(n // i)

    return arr
