n,b = input().split()
num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = 0
n = n[::-1]

for i,idx in enumerate(n):
    ans += (int(b)**i) * int(num.index(idx))
    
print(ans)
