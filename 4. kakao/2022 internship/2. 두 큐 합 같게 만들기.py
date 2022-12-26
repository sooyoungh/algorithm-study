
from collections import deque


def solution(queue1, queue2):
    answer = 0
    mid = (sum(queue1) + sum(queue2)) // 2
    leftSum = sum(queue1)

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    while queue1 and queue2:
        if leftSum > mid:
            tmp = queue1.popleft()
            leftSum -= tmp

        elif leftSum < mid:
            tmp = queue2.popleft()
            leftSum += tmp
            queue1.append(tmp)
        else:
            return answer

        answer += 1

    return -1


queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]

print(solution(queue2, queue1))
