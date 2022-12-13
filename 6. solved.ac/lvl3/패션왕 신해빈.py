from collections import defaultdict
import sys
input = sys.stdin.readline

tc = int(input())


def case():
    n = int(input())
    clothes = defaultdict(int)
    for _ in range(n):
        name, cate = input().split()
        clothes[cate] += 1

    answer = 1
    for i in clothes.values():
        answer *= (i+1)

    print(answer - 1)


for _ in range(tc):
    case()
