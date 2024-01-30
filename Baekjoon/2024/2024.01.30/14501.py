n = int(input())
t = []
p = []
for _ in range(n):
    ti,pi = map(int,input().split())
    t.append(ti)
    p.append(pi)
dp = [0 for _ in range(n+1)]

for i in range(n-1,-1,-1):
    # 날짜 초과
    if t[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(p[i] + dp[t[i] + i], dp[i+1])
print(dp[0])