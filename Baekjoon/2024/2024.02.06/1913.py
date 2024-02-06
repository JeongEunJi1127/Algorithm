import sys
input = sys.stdin.readline
n = int(input())
num = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)] 
standard = n**2

# 남동북서
dx = [1,0,-1,0]
dy = [0,1,0,-1]

x,y = 0,0
matrix[x][y] = standard
standard-=1
i = 0
x, y = x + dx[i], y + dy[i]

while standard>0:
    if x < 0 or x >= n or y < 0 or y >= n:
        x, y = x - dx[i], y - dy[i]
        i = (i+1)%4
    elif matrix[x][y] != 0:
        x, y = x - dx[i], y - dy[i]
        i = (i+1)%4
    else:
        matrix[x][y] == 0
        matrix[x][y] = standard
        standard-=1
    x, y = x + dx[i], y + dy[i]

ans = []
for iidx,i in enumerate(matrix):
    print(*i)
    for jidx,j in enumerate(i):
        if j == num:
            ans.append(iidx+1)
            ans.append(jidx+1)
print(*ans)
