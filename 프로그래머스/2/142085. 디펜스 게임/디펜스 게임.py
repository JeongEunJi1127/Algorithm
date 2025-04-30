# 16:00 ~ 

import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    
    # 한 명씩 지나가며 병사 수 빼기.
    for i in range(len(enemy)):
        n -= enemy[i]
        heapq.heappush(heap,-enemy[i])
        
        if n < 0:
            if k > 0: # 무적권 존재하면
                k -= 1
                n += -heapq.heappop(heap)
            else:
                return i
                   
    return len(enemy)