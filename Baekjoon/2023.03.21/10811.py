n, m = map(int,input().split())
ans = []
tmp = []
for i in range(n):
    ans.append(i+1)

for _ in range(m):
    a, b = map(int,input().split())
    tmp = ans[a-1:b]
    tmp = tmp[::-1]
    ans = ans[0:a-1]+tmp+ans[b:len(ans)]
        
for i in ans:
    print(i,end=' ')