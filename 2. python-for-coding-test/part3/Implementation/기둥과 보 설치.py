# 추가/삭제할 때 조건들이 가능한지 체크하는 함수 따로 만듦
# 2차원배열로 따로 안만들고 그냥 1차원배열에서 가능한지 여부 판별 가능

def possible(answer):
    for x,y, stuff in answer:
        # 기둥인 경우
        if stuff == 0:
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        # 벽인 경우
        if stuff == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True
            

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,op = frame
        # 삭제할 때
        if op == 0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        # 추가할 때
        if op == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
            
    return sorted(answer)
