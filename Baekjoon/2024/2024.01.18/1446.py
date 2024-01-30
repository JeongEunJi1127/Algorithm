import heapq
n,d = map(int,input().split())
inf = int(1e9)
graph = [[] for _ in range(d+1)]
distance = [inf] * (d+1)

for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    start, end, dist = map(int,input().split())
    if end <= d:
        graph[start].append((end,dist))

def dijkstra(s):
    q = []
    heapq.heappush(q,(0,s))
    distance[s] = 0
    while q:
        dis,now = heapq.heappop(q)
        if dis > distance[now]:
            continue
        for i in graph[now]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(0)
print(distance[d])