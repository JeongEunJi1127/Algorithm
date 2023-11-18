T = int(input())

for test_case in range(1, T + 1):
    n = list(input())
    ans = 1
    i = 0

    while len(n)>1:
        if n[0] != n[-1]:
            ans = 0
            break
        n = n[1:-1]
    print("#" + str(test_case),ans)