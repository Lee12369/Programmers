# 연속 펄스 부분 수열의 합
def solution(sequence):
    answer = 0
    N = len(sequence)
    dp = [sequence[0]]
    for i in range(1, N):
        if i % 2 == 0:
            num = dp[-1] + sequence[i]
        else:
            num = dp[-1] - sequence[i]    
        dp.append(num)
    
    max_num = max(dp)
    min_num = min(dp)
    
    answer = max(abs(max_num - min_num), abs(max_num), abs(min_num))
    
    return answer

