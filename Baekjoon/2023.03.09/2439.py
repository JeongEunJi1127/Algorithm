n= int(input())
cnt = n-1

for i in range(n):
    for _ in range(cnt):
        print(" ",end = "")
    for _ in range(n-cnt):
        print("*",end = "")
    print( )
    cnt -= 1

