matrix = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(4):
    lx,ly,rx,ry = map(int,input().split())

    for i in range(lx,rx):
        for j in range(ly,ry):
            matrix[i][j] = 1

ans = 0
for i in matrix:
    ans += i.count(1)        
print(ans)

