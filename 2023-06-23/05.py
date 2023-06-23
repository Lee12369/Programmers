from heapq import heappush, heapify, heappop
def solution(n, works):
    answer = 0
    N = len(works)
    heap = []
    for work in works:
        heappush(heap, (-work, work))
    
    for _ in range(n):
        x, y = heappop(heap)
        heappush(heap, (x + 1, y - 1))
        
        if heap[0][1] == 0:
            break
            
    for i in range(N):
        answer += (heap[i][1]) ** 2
        
    return answer