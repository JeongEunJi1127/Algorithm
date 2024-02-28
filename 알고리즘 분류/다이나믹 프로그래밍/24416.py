# 피보나치수
n = int(input())
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 1
cnt = 0

for i in range(3,n+1):
    cnt+=1
    dp[i] = dp[i-1] + dp[i-2]

print(dp[-1],cnt)