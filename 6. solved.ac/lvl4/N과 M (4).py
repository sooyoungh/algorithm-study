from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = []


def dfs(cnt, cur_num):  # 총 개수, 현재 숫자
    if cnt - 1 == m:
        print(" ".join(map(str, result)))
        return

    for num in range(cur_num, n+1):  # 현재 숫자도 선택 가능, 오름차순
        result.append(num)
        dfs(cnt+1, num)
        result.pop()


dfs(1, 1)
