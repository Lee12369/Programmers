# 여행 경로
from collections import defaultdict
def solution(tickets):
    answer = []
    N = len(tickets)
    dic = defaultdict(list)
    for i in range(N):
        dic[tickets[i][0]].append((tickets[i][1], i))
    
    for key in dic.keys():
        dic[key].sort()

    visited = [0 for _ in range(N)]
    def backtracking(lst, visited, start_airport):
        if len(lst) == (N + 1):
            answer.append(lst)
            return answer

        for tpl in dic[start_airport]:
            curr_airport, idx = tpl
            if visited[idx] == 0:
                visited[idx] = 1
                save_lst = lst + [curr_airport]
                save_start_airport = str(curr_airport)

                backtracking(save_lst, visited, save_start_airport)

                visited[idx] = 0
        return
    
    backtracking(["ICN"], visited, "ICN")
    answer = answer[0]
        
    return answer