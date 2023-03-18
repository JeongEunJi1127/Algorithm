a, b = map(int,input().split())
c = int(input())

if c >= 60 :
    a += c // 60
    b += c % 60
else:
    b+=c

if b>= 60:
    a += b // 60
    b -= 60
if a >= 24:
    a -= 24

print(a, b, end=" ")