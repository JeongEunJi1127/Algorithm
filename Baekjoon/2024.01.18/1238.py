import heapq
# 학생의 수, 도로의 수, 모일 마을번호
n,m,x = map(int, input().split())
inf = int(1e9)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start,end,t = map(int, input().split())
    graph[start].append((end,t))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance = [inf] * (n+1)
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

result = []
# i 마을에서 x마을까지 가는 다익스트라 최단거리 리스트 go, x 마을에서 i마을까지 돌아오는 다익스트라 최단거리 리스트 back을 구하고 더하기
for i in range(1,n+1):
    go = dijkstra(i)
    back = dijkstra(x)
    result.append(go[x]+back[i])
print(max(result))