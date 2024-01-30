n = int(input())
battle_power = list(map(int,input().split()))
battle_power = battle_power[::-1]
dp = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if battle_power[j] < battle_power[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))