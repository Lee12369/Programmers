def solution(routes):
    answer = 1
    routes.sort()
    std = routes[0][1]
    for lst in routes:
        start, end = lst[0], lst[1]
        if start > std:
            answer += 1
            std = int(end)
        if std > end:
            std = int(end)
        
    return answer