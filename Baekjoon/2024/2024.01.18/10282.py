import heapq
import sys
input = sys.stdin.readline
t = int(input())
inf = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance = [inf] * (n+1)
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in computer[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

for _ in range(t):
    # 컴퓨터 개수(노드), 의존성 개수(간선), 해킹당한 컴퓨터 번호(시작점)
    n,d,c = map(int,input().split())
    computer = [[] for _ in range(n+1)]
    for _ in range(d):
        # 컴퓨터 a가 컴퓨터 b를 의존하며, b가 감염되면 s초 후 a도 감염됨
        a,b,s = map(int,input().split())
        computer[b].append((a,s))
    result = dijkstra(c)
    cnt = 0
    max_result = 0
    for i in result:
        if i != inf:
            cnt+=1
            max_result = max(max_result,i)
            
    print(cnt,max_result)
