import heapq
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
inf = int(1e9)
graph = [[] for _ in range(n+1)]
path = [[1] for _ in range(n+1)]

for _ in range(m):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))

# s,e 는 검문소가 되는 노드, 고려하지 않고 continue 해준다
def dijkstra(graph,s,e):
    q = []
    distance = [inf] * (n+1)
    heapq.heappush(q,(0,1))
    distance[1] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            # 검문소에 걸리는지
            if s == now and e==i[0] or s==i[0] and e==now:
                continue
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # s가 0이 아니면 
                if not s:
                    gumunso[i[0]] = now
                heapq.heappush(q,(cost,i[0]))
    return distance

gumunso = [0 for _ in range(n+1)]
# s,e = 0,0 이므로 검문하지 않는다 / result = 최단 거리 시간
result = dijkstra(graph,0,0)[n]

ans = -1
end = n
while gumunso[end] != 0:
    start = gumunso[end]
    output = dijkstra(graph,start,end)[n]
    if output != inf:
        ans = max(ans,output-result)
    # 도시를 빠져나가지 못하게 만들 수 있음
    else:
        ans = -1
        break
    end = start
print(ans)