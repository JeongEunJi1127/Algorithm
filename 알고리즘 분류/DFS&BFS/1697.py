from collections import deque
n,k= map(int,input().split())
maxn = 100000
visited = [0] * (maxn+1)

def bfs(x):

    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        if x == k:
            return visited[x]
        for j in (x-1,x+1,x*2):
            if 0 <= j <= maxn and not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)

print(bfs(n))