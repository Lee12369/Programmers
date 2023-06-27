# 섬 연결하기
def solution(n, costs):
    answer = 0
    edges = []
    for lst in costs:
        start, end, cost = lst[0], lst[1], lst[2]
        edges.append((cost, start, end))    
    edges.sort()
    
    def find(parents, x):
        if parents[x] != x:
            parents[x] = find(parents, parents[x])
        return parents[x]
    
    def union(parents, a, b):
        a = find(parents, a)
        b = find(parents, b)
        if a < b:
            parents[b] = a
        else:
            parents[a] = b
            
    parents = [i for i in range(n)]
    for tpl in edges:
        cost, start, end = tpl
        if find(parents, start) != find(parents, end):
            union(parents, start, end)
            answer += cost
    
    return answer