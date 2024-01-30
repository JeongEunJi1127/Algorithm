import sys 
n,k = map(int,sys.stdin.readline().split())
prices = []
for _ in range(n):
    prices.append(int(sys.stdin.readline()))
prices.reverse()
ans = 0

for price in prices:
    if k == 0:
        break
    if k >= price:
        i = k//price
        ans += i
        k = k- (price * i)

print(ans) 
