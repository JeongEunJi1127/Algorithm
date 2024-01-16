a = int(input())
num = list(map(int,input().split()))
dp = [1] * a

for i in range(a):
    for j in range(i):
        if num[j] > num[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))