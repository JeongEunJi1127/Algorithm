import sys
input=sys.stdin.readline
t = int(input())

for _ in range(t):
    n, m= map(int,input().split())
    ans = 0

    for i in range(1,n):
        for j in range(i+1,n):
            if ((i**2 + j**2 + m) / (i*j)).is_integer():
                ans += 1

    print(ans)
