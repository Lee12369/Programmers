from collections import defaultdict
def solution(genres, plays):
    answer = []
    N = len(genres)
    dic = defaultdict(list)
    max_dic = defaultdict(int)
    
    for i in range(N):
        dic[genres[i]].append((plays[i], i))
        max_dic[genres[i]] += plays[i]
            
    lst = list(max_dic.items())
    lst.sort(key=lambda x: -x[1])
    
    for key in dic.keys():
        dic[key].sort(key=lambda x: -x[0])

    for genre, _ in lst:
        if len(dic[genre]) == 1:
            answer.append(dic[genre][0][1])
        else:
            answer.append(dic[genre][0][1])
            answer.append(dic[genre][1][1])

    return answer