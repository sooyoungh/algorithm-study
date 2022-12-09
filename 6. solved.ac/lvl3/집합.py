import sys
input = sys.stdin.readline

m = int(input())
data = set()

for _ in range(m):
    com = input().strip().split()
    if len(com) == 1:
        if com[0] == 'all':
            data = set([i for i in range(1, 21)])
        else:
            data = set()
        continue

    command, num = com[0], com[1]
    num = int(num)
    if command == 'add':
        data.add(num)
    elif command == 'remove':
        # data.remove(num) # remove : 해당 요소가 없으면 오류
        data.discard(num)
    elif command == 'check':
        print(1 if num in data else 0)
    elif command == 'toggle':
        if num in data:
            data.discard(num)
        else:
            data.add(num)
