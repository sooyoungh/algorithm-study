# 앞자리가 계속 높은 수가 되도록, 뒤에 더 높은 수면 앞 자리 빼기 -> K번까지
def solution(number, k):
    new_stack = []
    for num in number:
        while new_stack and num > new_stack[-1]:
            if k > 0:
                # 뒤가 더 높은 수일 경우, 먼저 넣은 수를 빼기
                new_stack.pop()
                k -= 1
            else:
                break
        # 일단 매번 스택에 넣기
        new_stack.append(num)
        
    # 더 빼야되는데 남은 수들은 다 작을 경우, 그냥 붙여야함!
    if k> 0:
        new_stack.pop()
        k-=1
        
    answer = "".join(new_stack)
        
    return str(answer)
