t = int(input())

for _ in range(t):
    h,w,n = map(int,input().split())
    ans = (n%h) * 100 + (n//h) + 1
    print(ans)
    