def solution(m, n, puddles):
    arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for lst in puddles:
        i, j = lst[1], lst[0]
        arr[i][j] = "pool"
    
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[1][1] = 1
                continue
            
            if arr[i][j] == 0: 
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000007
    
    answer = dp[n][m]

    return answer