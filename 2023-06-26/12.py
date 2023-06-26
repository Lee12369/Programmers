from itertools import permutations
from re import match

def solution(user_id, banned_id):
    lst_answer = []
    N = len(banned_id)
    for i in range(N):
        banned_id[i] = banned_id[i].replace('*','.')

    cases = list(permutations(user_id, N))
    for case in cases:
        check = True
        for i in range(N):
            if len(case[i]) == len(banned_id[i]) and match(banned_id[i], case[i]):
                continue
            else:
                check = False
                break
        if check:
            case = list(case)
            case.sort()
            if case not in lst_answer:
                lst_answer.append(case)
    
    answer = len(lst_answer)
    
    return answer