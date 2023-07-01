# 거스름돈
def solution(n, money):
    answer = 0
    money.sort()
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in money:
        for i in range(1, n + 1):
            idx = i - coin
            if idx >= 0:
                dp[i] += dp[idx]
        
    answer = dp[n] % 1000000007
    return answer