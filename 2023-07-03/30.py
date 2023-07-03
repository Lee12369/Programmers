# 인사고과
def solution(scores):
    answer = 1
    wanho1, wanho2 = scores[0]
    wanho_scores = sum(scores[0])
    scores.sort(key=lambda x : (-x[0], x[1]))

    threshold = 0
    for score in scores:
        if wanho1 < score[0] and wanho2 < score[1]:
            return -1
        
        if threshold <= score[1]:
            if wanho_scores < sum(score):
                answer += 1
            threshold = score[1]
    
    return answer