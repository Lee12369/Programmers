def solution(A, B):
    answer = 0
    N = len(A)
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    A_idx = 0
    B_idx = 0
    while A_idx < N:
        A_score = A[A_idx]
        B_score = B[B_idx]
        if A_score < B_score:
            A_idx += 1
            B_idx += 1
            answer += 1
        elif A_score >= B_score:
            A_idx += 1
        
    return answer