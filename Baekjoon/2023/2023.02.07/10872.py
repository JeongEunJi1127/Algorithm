n = int(input())
ans = 1

for _ in range(n):
    ans = ans * n
    n-=1
print(ans)