# 가장 먼 노드
from collections import defaultdict, deque
def solution(n, edge):
    dic = defaultdict(list)
    for lst in edge:
        dic[lst[0]].append(lst[1])
        dic[lst[1]].append(lst[0])
    
    visited = [0 for _ in range(n + 1)]
    
    queue = deque()
    queue.append(1)
    visited[1] = 1
    dist = 1
    while queue:
        save = deque()
        while queue:
            x = queue.popleft()
            for node in dic[x]:
                if visited[node] == 0:
                    visited[node] = dist
                    save.append(node)
        queue = save
        dist += 1
    
    max_num = max(visited)
    answer = visited.count(max_num)
    
    return answer