# 다단계 칫솔 판매
from collections import defaultdict
def solution(enroll, referral, seller, amount):
    answer = []
    graph = defaultdict(str)
    profits = defaultdict(int)
    N = len(enroll)
    for i in range(N):
        graph[enroll[i]] = referral[i]
    
    def distribution(seller, profit):
        if seller == '-' or profit < 10:
            return
        up_seller = graph[seller]
        up_profit = profit // 10
        profits[seller] -= up_profit
        profits[up_seller] += up_profit
        
        distribution(up_seller, up_profit)
        
    M = len(seller)
    for i in range(M):
        profit = amount[i] * 100
        profits[seller[i]] += profit
        distribution(seller[i], profit)
    
    for person in enroll:
        answer.append(profits[person])
    
    return answer