def solution(n, stations, w):
    answer = 0
    pre = 0
    length = w * 2 + 1
    for station in stations:
        empty_area = (station - w - 1) - pre
        
        share = empty_area // length
        remain = empty_area % length
        if remain == 0:
            answer += share
        elif remain > 0:
            answer += share + 1
        
        pre = station + w
    
    if pre < n:
        share = (n - pre) // length
        remain = (n - pre) % length
        if remain == 0:
            answer += share
        elif remain > 0:
            answer += share + 1
            
    return answer