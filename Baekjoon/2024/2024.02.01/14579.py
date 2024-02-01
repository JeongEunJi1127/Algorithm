a,b = map(int,input().split())
ans = 1
for i in range(a,b+1):
    cnt = 0
    for j in range(1,i+1):
        cnt+=j
    ans *= cnt
print(ans%14579)