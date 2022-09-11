import sys
input = sys.stdin.readline

d, n = map(int, input().split())
oven = [0] + list(map(int, input().split()))  # d 오븐깊이
pizza = [0] + list(map(int, input().split()))  # n 피자반죽 갯수

# 오븐 재정렬 - 아래가 가장 넓도록
for i in range(2, d+1):
    oven[i] = min(oven[i], oven[i-1])

pizza_pos = 1
# 오븐 바닥부터 피자 넣기
for i in range(d, 0, -1):
    if oven[i] >= pizza[pizza_pos]:
        pizza_pos += 1  # 다음 피자
    else:
        continue  # 다음 오븐

    if pizza_pos >= (n+1):
        print(i)  # 안되니까 i 높이에서 -1
        sys.exit(0)

print(0)
