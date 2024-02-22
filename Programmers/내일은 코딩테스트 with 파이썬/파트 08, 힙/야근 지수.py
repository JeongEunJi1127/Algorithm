import heapq

def solution(n, works):
    answer = 0
    heap = []
    if sum(works) > n:
        for i in works:
            heapq.heappush(heap,(-i,i))  
 
        while n >0:
            k = heapq.heappop(heap)
            heapq.heappush(heap,(k[0]+1,k[1]-1))  
            n-=1
        print(heap)
        
        for _ in range(len(heap)):
            answer += heapq.heappop(heap)[1] ** 2
    return answer