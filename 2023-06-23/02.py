def solution(triangle):
    dp = [0]
    N = len(triangle)
    for i in range(N):
        temp = []
        for j in range(i + 1):
            case1 = 0
            if j - 1 >= 0:
                case1 = triangle[i][j] + dp[j - 1]
            
            case2 = 0
            if j < len(dp):
                case2 = triangle[i][j] + dp[j]
            
            max_score = max(case1, case2)
            temp.append(max_score)
        
        dp = list(temp)
    
    answer = max(dp)
    return answer