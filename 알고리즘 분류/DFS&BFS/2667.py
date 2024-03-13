from collections import deque

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().rstrip())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(matrix,num):
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        if 1 in matrix[i]:
            idx_x,idx_y = i,matrix[i].index(1)
            queue = deque([(idx_x,idx_y)])
            visited[idx_x][idx_y] = True
            break
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny= x+dx[i],y+dy[i]
            if nx >= 0 and ny >=0 and nx <n and ny<n:
                if matrix[nx][ny] == 1 and not visited[nx][ny]:
                    matrix[nx][ny] = num
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    matrix[idx_x][idx_y] = num
    return matrix

num = 2
while True:
    cnt = 0
    for i in range(n):
        if 1 not in matrix[i]:
            cnt += 1
    if cnt == n:
        break  
    else:
        bfs(matrix,num)
        num+=1

print(num-2)
ans = []
for i in range(2,num):
    cnt = 0
    for j in matrix:
        cnt+= j.count(i)
    ans.append(cnt)
ans.sort()
for i in ans:
    print(i)