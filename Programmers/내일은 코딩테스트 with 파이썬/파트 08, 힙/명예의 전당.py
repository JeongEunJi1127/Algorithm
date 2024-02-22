import heapq
def solution(k, score):
    answer = []
    heap = []
    for s in score:
        heapq.heappush(heap,s)

        if len(heap) > k:
            heapq.heappop(heap)

        h = heapq.heappop(heap)

        answer.append(h)
        heapq.heappush(heap,h)
    return answer