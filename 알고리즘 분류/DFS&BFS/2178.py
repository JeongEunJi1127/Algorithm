# 최단 거리 -> BFS!
from collections import deque
n,m = map(int,input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().rstrip())))

#  우하좌상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

queue = deque([(0,0)])

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx,ny= x+dx[i],y+dy[i]
        if nx >= 0 and ny >=0 and nx <n and ny<m:
            if matrix[nx][ny] == 1:
                queue.append([nx,ny])
                matrix[nx][ny] = matrix[x][y] + 1
print(matrix[n-1][m-1])              