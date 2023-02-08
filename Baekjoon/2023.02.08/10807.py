n = int(input())
m = list(map(int, input().split()))
v = int(input())
ans = 0

for i in m:
    if i == v:
        ans += 1

print(ans)