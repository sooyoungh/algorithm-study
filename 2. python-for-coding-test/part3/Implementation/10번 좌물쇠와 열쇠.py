# 2차원 배열 90도 회전시키기***
def rotate(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = a[i][j]   # a -> result로 90도 회전
    return result

def check(new_lock):
    lock_length = len(new_lock)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] *(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
        key = rotate(key)
        # 시작점 반복문
        for x in range(1, n*2):
            for y in range(1, n*2):
                # 좌물쇠 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 체크
                if check(new_lock) == True:
                    return True
                # 좌물쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
