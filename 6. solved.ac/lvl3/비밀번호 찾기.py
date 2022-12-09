import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 기본 딕셔너리
data = {}

for _ in range(n):
    site, pwd = input().split()
    data[site] = pwd

for _ in range(m):
    find = input().strip()
    print(data[find])
