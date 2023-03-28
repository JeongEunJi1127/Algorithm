n = int(input()) 
mat = [[0 for _ in range(101)] for _ in range(101)]
cnt = 0

for _ in range(n):
    x, y = map(int,input().split())

    for i in range(x,x+10):
        for j in range(y,y+10):
            mat[i][j] = 1

for i in mat:
    for j in i:
        if j == 1:
            cnt+=1

print(cnt)

        



