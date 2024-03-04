t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    # 0층의 사람 수
    floor = [i for i in range(1,n+1)]

    while k != 0:
        lst = [0 for i in range(n)]
        for i in range(n):
            lst[i] = sum(floor[:i+1])
        floor = lst
        k-=1

    print(floor[n-1])