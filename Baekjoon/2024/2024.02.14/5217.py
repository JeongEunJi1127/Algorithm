t = int(input())
for i in range(t):
    n = int(input())
    print("Pairs for",n,end="")
    print(":",end=" ")
    for j in range(1, n//2+1):
        if j != n-j:
            if j != 1:
                print(",",end= " ")
            print(j,n-j,end="")
    print()