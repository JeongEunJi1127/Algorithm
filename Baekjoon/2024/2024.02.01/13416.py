import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for _ in range(n):
        a,b,c = map(int,input().split())
        if a<0 and b<0 and c<0:
            continue
        else:
            ans += max(a,b,c)
    print(ans)