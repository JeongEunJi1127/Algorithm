import math

n,k = map(int,input().split())
ans = 0

ans = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

print(ans)