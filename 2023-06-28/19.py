# 디스크 컨트롤러
from heapq import heappush, heappop, heapify
def solution(jobs):
    answer = 0
    N = len(jobs)
    jobs.sort()
    curr_time = 0
    total_time = 0
    idx = 0
    heap = []
    while idx < N:
        ask_time, taken_time = jobs[idx]
        # 현재 시간 기준으로 요청이 되었으면서 걸리는 시간이 짧은 기준으로 heap 정렬 
        if idx < N and ask_time <= curr_time:
            heappush(heap, (taken_time, ask_time))
            idx += 1
        # 현재 시간 기준으로 요청된 것들이 전부 들어간 heap. 이 안에서 가장 소요 시간이 짧은 것을 계산  
        elif heap and ask_time > curr_time:
            taken_time, ask_time = heappop(heap)
            curr_time += taken_time
            total_time += curr_time - ask_time
        # 현재 시간 기준으로 heap 안에 들어있는 것이 없을 경우 시간을 추가하여 heap에 값이 추가 되도록 유도
        elif heap == []:
            curr_time += 1
    
    # jobs 안에 모든 값들이 heap에 저장되었으나 아직 계산되지 않은 heap 안에 값들을 마저 정리
    while heap:
        taken_time, ask_time = heappop(heap)
        curr_time += taken_time
        total_time += curr_time - ask_time
        
    
    answer = total_time // N
    
    return answer