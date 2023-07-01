def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    K = len(skill)
    
    sum_skills = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(K):
        [type, r1, c1, r2, c2, degree] = skill[i]
        if type == 1:
            degree *= -1
        sum_skills[r1][c1] += int(degree)
        sum_skills[r2 + 1][c2 + 1] += int(degree)
        sum_skills[r1][c2 + 1] += int(-degree) 
        sum_skills[r2 + 1][c1] += int(-degree)
        
    for i in range(N + 1):
        for j in range(1, M + 1):
            sum_skills[i][j] += sum_skills[i][j - 1]
    
    for j in range(M + 1):
        for i in range(1, N + 1):
            sum_skills[i][j] += sum_skills[i - 1][j]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] + sum_skills[i][j] > 0:
                answer += 1

    return answer