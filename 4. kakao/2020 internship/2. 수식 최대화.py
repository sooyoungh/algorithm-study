from itertools import permutations
import copy

def solution(expression):
    answer = 0
    ori_num = []
    ori_op = []

    op_sample = ['*', '+', '-']
    prev_num = ''
    # 1. 분리하기
    for case in expression:
        if case in op_sample:
            ori_op.append(case)
            ori_num.append(int(prev_num))
            prev_num = ''
        else:
            prev_num += case
    ori_num.append(int(prev_num))
    n = len(ori_num)

    # 2. 연산 우선 순위
    max_result = 0
    for case in permutations(op_sample, 3):  # (+, -, *) 등등
        num = copy.deepcopy(ori_num)
        op = copy.deepcopy(ori_op)
        for tmp_op in case:  # ex. +, -, *
            for i in range(len(op)):
                if op[i] == tmp_op:
                    j = i+1
                    while num[j] == None:
                        j += 1
                        if num[j] != None:
                            break
                    if tmp_op == '*':
                        num[j] = num[i] * num[j]
                    elif tmp_op == '+':
                        num[j] = num[i] + num[j]
                    elif tmp_op == '-':
                        num[j] = num[i] - num[j]
                    num[i] = None
                    op[i] = None
        if num[n-1] < 0:
            num[n-1] *= (-1)
        max_result = max(max_result, num[n-1])

    return max_result
