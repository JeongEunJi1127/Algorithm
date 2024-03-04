def dfs(x):
    visited[x] = True
    y = p[x]
    if not visited[y]:
        dfs(y)
        
t = int(input())
for _ in range(t):
    n = int(input())
    p = [0] + list(map(int,input().split()))
    visited = [False] * (n+1)
    ans = 0

    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)
            ans += 1
    print(ans)

