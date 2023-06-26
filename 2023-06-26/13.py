from collections import defaultdict
def solution(gems):
    answer = []
    N = len(gems)
    target = len(set(gems))
    dic = defaultdict(int)
    left = 0
    right = 0
    cnt = 0
    while left < N:
        if right < N and cnt < target:
            if dic[gems[right]] == 0: 
                cnt += 1
            dic[gems[right]] += 1
            right += 1    
        elif right == N or cnt > target:
            if dic[gems[left]] == 1:
                cnt -= 1
            dic[gems[left]] -= 1
            left += 1
        
        while cnt == target:
            length = right - left
            answer.append((length, [left + 1, right]))
            if dic[gems[left]] == 1:
                cnt -= 1
            dic[gems[left]] -= 1
            left += 1

    answer.sort(key=lambda x : x[0])
    answer = answer[0][1]
    return answer