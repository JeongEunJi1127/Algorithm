import sys
input = sys.stdin.readline

t = int(input())

def solution():
    for _ in range(t):
        n = int(input())
        coins = list(map(int, input().split()))
        coins.insert(0, 0)
        m = int(input())

        dp = [[0] * (m+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1

        for j in range(1, n+1):
            for i in range(1, m+1):
                dp[j][i] = dp[j-1][i]
                if i-coins[j] >= 0:
                    dp[j][i] += dp[j][i-coins[j]]

        print(dp[n][m])

solution()