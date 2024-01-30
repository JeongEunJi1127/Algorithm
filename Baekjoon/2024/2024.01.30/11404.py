import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = [[int(1e9) for _ in range(n)] for _ in range(n)]

for i in range(n):
    lst[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    lst[a-1][b-1] = min(lst[a-1][b-1],c)

for i in range(n):
    for j in range(n):
        for k in range(n):
            lst[j][k] = min(lst[j][k], lst[j][i]+lst[i][k])

for i in lst:
    for j in i:
        if j == int(1e9):
            print(0,end=" ")
        else:
            print(j,end=" ")
    print( )
