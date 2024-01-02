import sys

t = int(sys.stdin.readline())
sosu = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2,1000001):
    if check[i] == 0:
        sosu.append(i)
        for j in range(2*i,1000001,i):
            check[j]=1

for _ in range(t):
    n = int(sys.stdin.readline())
    cnt = 0
    for i in sosu:
        if i >= n:
            break
        if not check[n-i] and i <= n-i:
            cnt+=1
    print(cnt)
