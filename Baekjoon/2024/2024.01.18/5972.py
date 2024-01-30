import heapq
# 헛간, 길
n,m = map(int, input().split())
inf = int(1e9)
distance = [inf] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    # a,b 헛간 사이의 길의 소의 개수
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(1)
print(distance[n])