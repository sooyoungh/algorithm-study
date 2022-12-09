import sys
input = sys.stdin.readline

t = int(input())


def fibo(n):
    zero = [1, 0, 1]
    one = [0, 1, 1]

    if n > 2:
        for i in range(2, n):
            zero.append(zero[i-1] + zero[i])
            one.append(one[i-1] + one[i])

    print(zero[n], one[n])


for _ in range(t):
    n = int(input())
    fibo(n)


# -----피보나치 수열
# 1, 1, 2, 3, 5 ...
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
