def plus(ii,jj): # 함수화!!!! 4중 포문보다 보기 좋다
    global m
    global lst
    cnt = 0
    for k in range(m):
        for h in range(m):
            cnt += lst[ii + k][jj + h]
    return cnt

t = int(input())

for test_case in range(1,t+1):
    n,m = map(int,input().split())
    lst = []
    ans = 0
    for _ in range(n):
        lst.append(list(map(int,input().split())))

    for i in range(n-m+1):
        for j in range(n-m+1):
            ans = max(ans,plus(i,j))
    print("#"+str(test_case), ans)