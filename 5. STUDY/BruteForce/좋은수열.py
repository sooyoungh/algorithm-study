# dfs + 문자열체크
import sys
input = sys.stdin.readline

n = int(input())

result = []


def check(tmp):
    for i in range(1, len(tmp)//2 + 1):
        if tmp[-i:] == tmp[-(i*2):-i]:
            return False
    return True


def dfs(idx):
    global result
    if idx == n:  # 처음 찾은 좋은 수열이 최소이므로 답!
        print(''.join(map(str, result)))
        sys.exit()  # 리턴하면 계속 dfs 탐색

    for i in range(1, 4):  # dfs 계속
        result.append(i)
        if check(result):
            dfs(idx+1)
        result.pop()


dfs(0)
