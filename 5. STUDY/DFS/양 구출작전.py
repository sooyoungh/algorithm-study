import sys
sys.setrecursionlimit(10**6)

s = sys.stdin.readline
n = int(s())
graph = [0] * (n+1)  # 늑대/양 정보
relation = [[] for _ in range(n+1)]  # 부모-자식 관계

for i in range(2, n+1):
    tmp, num, par = s().split()
    if tmp == 'W':
        num = (-1) * int(num)
    graph[i] = int(num)
    relation[int(par)].append(i)


def dfs(start):
    answer = graph[start]

    for next in relation[start]:
        answer += dfs(next)

    if answer < 0:
        return 0
    else:
        return answer


result = dfs(1)
print(result)
