# 징검다리 건너기
def solution(stones, k):
    answer = 0
    N = len(stones)
    left = 1
    right = max(stones)
    while left <= right:
        check = "left"
        cnt = 0
        mid = (left + right) // 2
        for stone in stones:
            if (stone - mid) <= 0:
                cnt += 1
            else:
                cnt = 0
            
            if cnt == k:
                check = "right"
                break
        
        if check == 'right':
            right = mid - 1
        else:
            left = mid + 1
            
    answer = left
    return answer