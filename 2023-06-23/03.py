def solution(n, s):
    answer = []
    cnt  = s % n
    number = s // n
    if cnt > 0:
        for _ in range(n - cnt):
            answer.append(number)
        
        for _ in range(cnt):
            answer.append(number + 1)
        
    elif cnt == 0:
        for _ in range(n):
            answer.append(number)
    
    if 0 in answer:
        answer = [-1]

    return answer