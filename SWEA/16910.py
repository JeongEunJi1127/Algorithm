T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    cnt = 0

    for i in range(n+1):
        for j in range(n+1):
            if i*i + j*j <= n*n:
                cnt+=1
    cnt *= 4
    cnt -= 3 + (n * 4)

    print("#"+str(test_case),cnt)