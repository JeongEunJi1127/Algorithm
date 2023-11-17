T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    ans = 0

    for i in range(1,n+1):
        if i % 2 == 1:
            ans += i
        else:
            ans -= i

    print("#"+str(test_case), ans)