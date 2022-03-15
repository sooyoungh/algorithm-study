# 1. 이코테 교재 풀이 활용
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    #parent = [0] *(n+1)
    #for i in range(1, n+1):
    #    parent[i] = i
    
    parent = [i for i in range(n+1)] # 여기서는 노드가 0부터라서 n까지 해도 됨!
    
    costs.sort(key = lambda x : x[2])
    
    for tmp in costs:
        a,b,cost = tmp
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a,b)
            answer += cost

    
    print(costs)
    return answer

# 2. 크루스칼 다른 풀이 - set, update 활용!
def solution(n, costs): 
    answer = 0 
    costs.sort(key = lambda x: x[2]) # 비용기준으로 오름차순 정렬 
    connect = set([costs[0][0]]) # 연결을 확인하는 집합 Kruskal 알고리즘으로 최소 비용 구하기 
    while len(connect) != n: 
        for cost in costs: 
            if cost[0] in connect and cost[1] in connect: 
                continue 
            if cost[0] in connect or cost[1] in connect: 
                connect.update([cost[0], cost[1]])
                answer += cost[2] 
                break
    return answer
