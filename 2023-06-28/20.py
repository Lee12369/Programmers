# 합승 택시 요금
from heapq import heappop, heappush
from collections import defaultdict
def solution(n, s, a, b, fares):
    graph = defaultdict(dict)
    for fare in fares:
        start, end, cost = fare[0], fare[1], fare[2]
        graph[start].update({end : cost})
        graph[end].update({start : cost})

    INF = int(1e9)
    def djikstra(graph, start):
        distances = [INF for _ in range(n + 1)]
        distances[start] = 0
        heap = []
        heappush(heap, (distances[start], start))
        
        while heap:
            curr_dist, curr_destination = heappop(heap)
            if distances[curr_destination] < curr_dist:
                continue
            
            for next_destination, next_dist in graph[curr_destination].items():
                sum_dist = curr_dist + next_dist
                if sum_dist < distances[next_destination]:
                    distances[next_destination] = sum_dist
                    heappush(heap, (sum_dist, next_destination))
        
        return distances
    
    answer = INF
    s_distances = djikstra(graph, s)
    for i in range(1, n + 1):
        ab_distances = djikstra(graph, i)
        cost = s_distances[i] + ab_distances[a] + ab_distances[b] 
        if answer > cost:
            answer = cost
    
    return answer