from collections import deque
n = int(input())

data = [i for i in range(1, n+1)]
data = deque(data)

while (len(data) != 1):
    data.popleft()
    move_card = data.popleft()
    data.append(move_card)

print(data[0])

# ++ 규칙 발견해서 식세우기
