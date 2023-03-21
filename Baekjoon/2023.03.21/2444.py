n = int(input())
m = (2*n)-1

for i in range(m):
    a= 1+(i*2)
    if a>m:
        a= m - ((i-(m//2))*2)
    for j in range(0,abs((m-1-(i*2))//2)):
        print(" ",end="")
    for j in range(abs((m-1-(i*2))//2),abs((m-1-(i*2))//2)+a):
        print("*",end="")
    for j in range(abs((m-1-(i*2))//2)+a,m):
        print("",end="")
    print( )