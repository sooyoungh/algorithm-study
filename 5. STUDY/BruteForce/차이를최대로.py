from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = -1


# 1) 순열
arr_list = list(permutations(arr, n))

for i in range(len(arr_list)):
    tmp = 0
    arr = arr_list[i]

    for j in range(len(arr)-1):
        tmp += abs(arr[j] - arr[j+1])
    answer = max(answer, tmp)


print(answer)


# 2) dfs
def dfs(tmp, visited):
    global answer
    if len(tmp) == n:
        total = 0
        for i in range(n-1):
            total += abs(tmp[i]-tmp[i+1])
        answer = max(answer, total)

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            tmp.append(arr[i])
            dfs(tmp, visited)
            visited[i] = 0
            tmp.pop()


answer = 0
visited = [0] * n
dfs([], visited)

print(answer)
