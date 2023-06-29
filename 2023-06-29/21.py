# 입국 심사
def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n
    while left < right:
        mid = (left + right) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
        
        if cnt >= n:
            right = mid
        else:
            left = mid + 1
    
    answer = left
    return answer