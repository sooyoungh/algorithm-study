import copy
import sys
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))


# 메모리 초과 -> DP로 풀이!
# 계속 값 갱신하기
max_result = copy.deepcopy(graph)
min_result = copy.deepcopy(graph)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    max_result = [a + max(max_result[0], max_result[1]), b +
                  max(max_result), c + max(max_result[1], max_result[2])]
    min_result = [a + min(min_result[0], min_result[1]), b +
                  min(min_result), c + min(min_result[1], min_result[2])]

print(max(max_result), min(min_result))
