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
    parent = [0] *(n+1)
    for i in range(1, n+1):
        parent[i] = i
    
    costs.sort(key = lambda x : x[2])
    
    for tmp in costs:
        a,b,cost = tmp
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a,b)
            answer += cost

    
    print(costs)
    return answer
