def perfectnum(i):
    lst = []
    cnt = 0

    for j in range(1,i+1):
        if i % j == 0 and j != i:
            lst.append(j)
    for k in lst:
        cnt+=k

    if cnt == i:
        print(i,"=",end=" ")
        for k in lst:
            print(k,end=" ")
            if k != lst[-1]:
                print("+",end=" ")
        return 
    else:
        print(i, "is NOT perfect.")
        return 

while True:
    n = int(input())

    if n == -1:
        break
    perfectnum(n)
        
