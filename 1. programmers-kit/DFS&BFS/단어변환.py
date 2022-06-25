# BFS
# 단어 하나가 다른건 두 노드가 연결된 간선이 있는 것과 같음!
# 1. 
from collections import deque
def solution(begin, target, words):
    answer = 0
    check = [False for i in range(len(words))] # 방문 여부 체크용
    q = deque()
    q.append([begin, 0])
    
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
            
        for k in range(len(words)):
            tmp = 0
            if check[k] == True:
                continue
            for i in range(len(word)):
                if word[i] != words[k][i]:
                    tmp += 1
            if tmp == 1:
                q.append([words[k], cnt+1])
                check[k] = True

    
    return answer
  
  # 2.  함수화
from collections import deque
def solution(begin, target, words):
    n = len(words)
    visited = [False] * n
    
    def check(origin, new):
        n = len(origin)
        cnt = n
        for i in range(n):
            if origin[i] != new[i]:
                cnt -= 1

        if cnt == n-1:
            return True
        else:
            return False
    
    def bfs():
        q = deque()
        q.append([begin, 0])
        while q:
            now, cnt = q.popleft()
            if now == target:
                print(cnt)
                break

            for new in words:
                if not visited[words.index(new)]:
                    if check(now, new):
                        q.append([new, cnt+1])

        return cnt
    
    if not (target in words):
        return 0
    else:
        answer = bfs()
    return answer
  
