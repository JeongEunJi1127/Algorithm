import sys
# 처음 써보는데 이거 써야 recursion error 가 안난다
sys.setrecursionlimit(10**7)

input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(n):
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i) 

cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)