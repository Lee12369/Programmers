# 부대복귀
from heapq import heappush, heappop
def solution(n, roads, sources, destination):
    answer = []
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    
    def djikstra(start):
        heap = []
        heappush(heap, (0, start))
        distances[start] = 0
        while heap:
            dist, curr = heappop(heap)
            if distances[curr] < dist:
                continue
            
            for i in graph[curr]:
                cost = dist + 1
                if cost < distances[i]:
                    distances[i] = cost
                    heappush(heap, (cost, i))
        
    
    distances = [INF for _ in range(n + 1)]
    djikstra(destination)
    for start in sources:
        dist = distances[start]
        if dist == INF:
            dist = -1
        answer.append(dist)
        
    return answer