n = int(input())
dp = [1] * (n+1)
lst = list(map(int,input().split()))

for i in range(1,n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))