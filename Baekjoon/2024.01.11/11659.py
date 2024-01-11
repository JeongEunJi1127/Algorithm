import sys
n,m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
dp = [0] * (n+1)
for k in range(n):
    dp[k+1] = dp[k]+lst[k]
for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())

    print(dp[j]-dp[i-1])