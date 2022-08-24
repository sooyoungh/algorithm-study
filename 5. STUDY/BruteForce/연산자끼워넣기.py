# dfs
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_val = -1e9
min_val = 1e9


def dfs(index, tmp):
    global max_val, min_val, add, sub, mul, div
    if index == n:  # dfs 종료
        min_val = min(min_val, tmp)
        max_val = max(max_val, tmp)
        return

    if add > 0:
        add -= 1
        # tmp를 매개변수로 받는 게 깔끔 => 그냥 매개변수로 전달 안받고 add 처럼 더하고 빼도 됨
        dfs(index+1, tmp + data[index])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(index+1, tmp - data[index])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(index+1, tmp * data[index])
        mul += 1
    if div > 0:
        div -= 1
        dfs(index+1, int(tmp/data[index]))
        div += 1


dfs(1, data[0])
print(max_val)
print(min_val)
