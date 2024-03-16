n = int(input())
c = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(c):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

lst = []
visited = [False] * (n+1)
def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:       
            lst.append(i)
            dfs(i)
    return lst

print(len(dfs(1)))