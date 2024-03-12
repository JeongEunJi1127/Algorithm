import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

for i in range(1,n+1):
    t,p = map(int,input().split())
    dp[i] = max(dp[i-1],dp[i])
    # 기간내에 끝나면
    if i+t-1 <= n:
        dp[i+t-1] = max(dp[i+t-1],dp[i-1]+p)

print(dp[-1])


