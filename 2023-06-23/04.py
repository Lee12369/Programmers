from collections import defaultdict, deque

def dfs(lst, visited, dic):
    queue = deque(lst)
    while queue:
        x = queue.pop()
        visited[x] = 1
        for y in dic[x]:
            if visited[y] == 0:
                visited[y] = 1
                queue.append(y)

def solution(n, computers):
    answer = 0
    dic = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                dic[i + 1].append(j + 1)

    visited = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(dic[i], visited, dic)
            answer += 1
            
    return answer