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
        x = y
        y = x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


# ------3. 유클리드 호제법 - 공식------
print(math.lcm(n, m))
print(math.gcd(n, m))
