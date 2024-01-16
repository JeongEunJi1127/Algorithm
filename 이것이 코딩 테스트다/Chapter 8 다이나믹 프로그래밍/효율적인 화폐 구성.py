n,m = map(int,input().split())
money = [int(input()) for _ in range(n)]
d = [10001] * 10000
d[0] = 0 

for i in range(n):
    for j in range(money[i],m+1):
        if d[j-money[i]] != 10001:
            d[j] = min(d[j],d[j - money[i]]+1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])