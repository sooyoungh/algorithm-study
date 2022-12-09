import sys
input = sys.stdin.readline

n, m = map(int, input().split())
not_hear = set()
not_watch = set()

for _ in range(n):
    tmp = input().strip()
    not_hear.add(tmp)

for _ in range(m):
    tmp = input().strip()
    not_watch.add(tmp)

answer = not_hear & not_watch

answer = list(answer)
answer.sort()
print(len(answer))
for i in answer:
    print(i)
