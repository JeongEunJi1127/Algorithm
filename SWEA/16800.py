import math
t = int(input())


for test_case in range(1, t+1):
    n = int(input())
    ans = n

    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            ans = min(ans, n//i+i-2)

    print("#"+str(test_case),ans)