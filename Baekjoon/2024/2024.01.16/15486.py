import sys
n = int(sys.stdin.readline())
dp = [0] * (n+1)

for i in range(1,n+1):
    t,p = map(int,sys.stdin.readline().split())
    # 이전 수익과 현재 수익 비교
    dp[i] = max(dp[i-1],dp[i])
    # 현재 일차 + 상담이 마무리되는 날이 (n+1)보다 작거나 같을때
    if t+i-1 <= n:
        # 상담 종료일의 최대 수익 = max(이전까지의 수익+현재수익, 상담 종료일의 최대 수익)
        dp[t+i-1] = max(dp[t+i-1],dp[i-1]+p)

print(dp[-1])