from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [-1 for _ in range(n+1)]

def bfs(graph,start,distance):
    queue = deque([start])
    distance[start] = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[v] + 1
   
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

bfs(graph,x,distance)

if distance.count(k) == 0:
    print(-1)
else:
    ans = []
    for index,i in enumerate(distance):
        if i == k:
            ans.append(index)
    ans.sort()
    for i in ans:
        print(i)