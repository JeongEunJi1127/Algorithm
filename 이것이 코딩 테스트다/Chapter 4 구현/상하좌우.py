n = int(input())
plan = list(input().split())
x,y = 1,1
nx,ny = 0,0

dx = [0,0,-1,1] # 좌우하상
dy = [-1,1,0,0]
moves = ["L", "R", "U", "D"]

for i in plan:
    for j in range(4):
        if i == moves[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx <1 or nx > n or ny < 1 or ny > n:
        continue
    x,y = nx,ny

print(nx,ny)
