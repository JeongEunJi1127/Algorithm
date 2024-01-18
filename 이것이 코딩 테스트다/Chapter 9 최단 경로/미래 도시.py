from pprint import pprint
# 노드의 개수, 간선의 개수
n,m = map(int,input().split())
infinite = int(1e9)
graph = [[infinite for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    c1, c2 = map(int,input().split())
    graph[c1][c2] = 1
    graph[c2][c1] = 1

X, K = map(int,input().split())

# 모든 노드가 중간노드 i를 거쳐가는 경우 구하기
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])

distance = graph[1][K] + graph[K][X]

if distance >= infinite:
    print(-1)
else:
    print(distance)