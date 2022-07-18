from collections import defaultdict


def solution(id_list, report, k):
    # 중복 신고 제거
    report = list(set(report))

    n = len(id_list)
    report_n = len(report)
    answer = [0] * n

    warned = defaultdict(int)  # {신고 당한 사람 : 횟수}
    data = defaultdict(set)  # {신고자 : 신고 당한 사람}

    for i in range(report_n):
        a, b = report[i].split()
        # if not b in data[a]:  # 중복 제거 안했을 경우 필요!
            # warned[b] += 1
        warned[b] += 1
        data[a].add(b)  # 어차피 set이니까

    # for key, values in data.items():
    #     for v in values:
    #         if warned[v] >= k:
    #             answer[id_list.index(key)] += 1
    
    for i in id_list:
        result = 0
        for u in data[i]:
            if warned[u]>=k:
                result +=1
        answer.append(result)

    return answer
