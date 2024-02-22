import heapq
def solution(scoville, K):
    cnt = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
    
    while heap[0] < K:
        if len(heap) <= 1:
            break
        cnt += 1
        sco = heapq.heappop(heap) + (heapq.heappop(heap) * 2)
        heapq.heappush(heap,sco)
        
    if heap[0] < K:
        cnt = -1
    return cnt