from collections import defaultdict, deque
def bfs(queue, words, visited, N, target):
    temp = deque()
    while queue:
        begin = queue.popleft()
        for word in words:
            if visited[word] == 0:
                cnt = 0
                check = True
                for i in range(N):
                    if word[i] != begin[i]:
                        cnt += 1
                    if cnt > 1:
                        check = False
                        break

                if check == True:
                    visited[word] = 1
                    temp.append(word)
                    if word == target:
                        return temp, "Found"
    
    return temp, "notFound"

def solution(begin, target, words):
    answer = 1
    N = len(begin)
    
    queue = deque([begin])
    visited = defaultdict(int)
    visited[begin] = 1    
    
    while queue:
        queue, check = bfs(queue, words, visited, N, target)
        if check == "Found":
            return answer
        
        answer += 1
    return 0