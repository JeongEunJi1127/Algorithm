from collections import deque

n = int(input())
ans = 0
tips = []
for _ in range(n):
    tips.append(int(input()))
tips.sort(reverse=True)

rank = 1
for tip in tips:
    if tip - (rank -1) >= 0:
        ans += tip - (rank -1)
    rank += 1
print(ans)