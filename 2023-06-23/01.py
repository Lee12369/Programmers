from heapq import heappush, heappop, heapify
def min_heap(heap, D):
    if D == 1:
        temp = []
        for num in heap:
            heappush(temp, -num)
        heappop(temp)
        return temp
    
    heappop(heap)
    return heap

def max_heap(heap, D):
    if D == -1:
        temp = []
        for num in heap:
            heappush(temp, -num)
        heappop(temp)
        return temp
    
    heappop(heap)
    return heap
    
def solution(operations):
    heap = []
    answer =[]
    D = -1
    for command in operations:
        word, num = command.split()
        num = int(num)
        if word == 'I':
            if D == -1:
                heappush(heap, num)
            elif D == 1:
                heappush(heap, -num)
        
        elif word == 'D':
            if heap and num == 1:
                heap = max_heap(heap, D)
                D = 1
                
            elif heap and num == -1:
                heap = min_heap(heap, D)
                D = -1
        
    if heap:
        max_score = max(heap)
        min_score = min(heap)
        if D == 1:
            max_score, min_score = -min_score, -max_score

        answer = [max_score, min_score]
    
    else:
        answer = [0,0]
    
        
    return answer