import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

cnt = 0
while n > 1:
    pivot = (2**n) // 2  # 4분면 구역 나누는 기준
    if r < pivot and c >= pivot:
        cnt += pivot**2
        c -= pivot
    elif r >= pivot and c < pivot:
        cnt += (pivot**2) * 2
        r -= pivot
    elif r >= pivot and c >= pivot:
        cnt += (pivot**2) * 3
        c -= pivot
        r -= pivot
    # 1 사분면은 따로 계산 X
    n -= 1

# 최종 2 * 2인 배열에서의 위치 -> 추가적으로 cnt 계산
if r == 0 and c == 0:
    print(cnt)
elif r == 0 and c == 1:
    print(cnt + 1)
elif r == 1 and c == 0:
    print(cnt + 2)
elif r == 1 and c == 1:
    print(cnt + 3)
