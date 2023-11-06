n = int(input())
p = list(map(int,input().split()))
p.sort()
ans = 0
prv = 0

for i in p:
    ans += i+prv
    prv = i+prv
print(ans)