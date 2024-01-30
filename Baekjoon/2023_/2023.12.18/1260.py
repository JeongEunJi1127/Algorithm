from collections import deque
n,m,v = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

for _ in range(m):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def Dfs(lst,v,visited):
    visited[v] = True
    print(v,end=" ")
    for i in range(1,n+1):
        if not visited[i] and lst[v][i]==1:
            Dfs(lst,i,visited)

def Bfs(lst,v,visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        k = queue.popleft()
        print(k,end=" ")
        for i in range(1,n+1):
            if not visited[i] and lst[k][i] == 1:
                queue.append(i)
                visited[i] = True

Dfs(graph,v,dfs_visited)
print( )
Bfs(graph,v,bfs_visited)