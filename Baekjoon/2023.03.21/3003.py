# 킹, 퀸, 룩, 비숍, 나이트, 폰
ipt = list(map(int,input().split()))
ans = [1, 1, 2, 2, 2, 8]

for idx,i in enumerate(ans):
    if ipt[idx] != i:
        ans[idx] = i - ipt[idx]
    else:
        ans[idx] = 0

for i in ans:
    print(i,end=' ')
    

