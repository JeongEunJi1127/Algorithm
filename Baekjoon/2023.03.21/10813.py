n, m = map(int,input().split())
ans = []
for i in range(n):
    ans.append(i+1)

for _ in range(m):
    a, b = map(int,input().split())
    tmp = ans[a-1]
    ans[a-1] = ans[b-1]
    ans[b-1] = tmp

for i in ans:
    print(i,end=' ')