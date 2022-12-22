import sys
input = sys.stdin.readline

number = int(input())
m = int(input())
broken_btn = list(map(int, input().split()))

# 버튼 누르는 방법 1 - + => 1만큼 이동
# 버튼 누르는 방법 2 - +숫자 => 해당 숫자만큼 이동

answer = abs(number - 100)  # 경우1) 현재 100번에서 +, -만으로 이동할 수 있는 경우
for case in range(1000001):  # 경우2) 0~50만, 경우3) 50만~100만까지
    flag = True
    for i in str(case):  # 해당 숫자를 다 누를 수 있는 지
        if int(i) in broken_btn:
            flag = False
            break
    if flag:
        # 숫자 i 입력한 횟수 + 숫자 i 에서 구하는 number까지의 거리
        new_answer = len(str(case)) + abs(number - case)
        answer = min(answer, new_answer)

print(answer)
