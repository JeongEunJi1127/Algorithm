# 이친수 문제
n = int(input())

dp = [0] * (n+1)
# 0으로 시작하지 않는다
dp[1] += 1

for i in range(2,n+1):
    # 1이 연속으로 두번 나타나지 x
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])