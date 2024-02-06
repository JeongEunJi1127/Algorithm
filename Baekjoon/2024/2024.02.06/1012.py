from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or ny <0 or nx >= n or ny >= m:
                continue
            if matrix[nx][ny] == 1:
                queue.append((nx,ny))
                matrix[nx][ny] = 0

for _ in range(t):
    m,n,k = map(int,input().split())
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x,y = map(int,input().split())
        matrix[y][x] = 1

    # 동남서북
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                bfs(i,j)
                cnt += 1    
                
    print(cnt)
