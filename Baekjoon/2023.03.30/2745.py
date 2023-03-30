n,b = input().split()
num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = 0
n = n[::-1]

for i,idx in enumerate(n):
    ans += (int(b)**i) * int(num.index(idx))
    
print(ans)
# N, b = input().split()
# ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# N = N[::-1]
# result = 0

# for i,n in enumerate(N):
#     result += (int(b)**i)*(ary.index(n))
# print(result)