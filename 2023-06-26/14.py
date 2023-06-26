def solution(sticker):
    answer = []
    N = len(sticker)
    dp = [0 for _ in range(N)]
    
    # 첫 번째 숫자를 뽑았을 경우
    dp = [0 for _ in range(N)]
    dp[0] = sticker[0]
    for i in range(1, N - 1):
        case1 = dp[i - 1]
        case2 = sticker[i] + dp[i - 2]
        dp[i] = max(case1, case2)
    answer1 = max(dp)
    
    # 첫번째 숫자를 뽑지 않을 경우
    dp = [0 for _ in range(N)]
    dp[0] = 0
    for i in range(1, N):
        case1 = dp[i - 1]
        case2 = sticker[i] + dp[i - 2]
        dp[i] = max(case1, case2)
    answer2 = max(dp)
    
    answer = max(answer1, answer2)
    return answer