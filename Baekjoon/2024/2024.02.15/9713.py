t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for i in range(n):
        if i % 2 == 1:
            ans += i
    print(ans+n)