while True:
    data = input()

    if data == '0':
        break

    flag = 'yes'

    n = len(data)
    for i in range(n//2):
        if (data[i] != data[n-1-i]):
            flag = 'no'
            break

    print(flag)


# 문자열[시작:끝:규칙]
if n == n[::-1]:
    flag = 'no'
