bx,by = map(int,input().split())
dx,dy = map(int,input().split())
jx,jy = map(int,input().split())

b = max(abs(jx-bx),abs(jy-by))
d = abs(jx-dx)+abs(jy-dy)
if b == d:
    print("tie")
elif b<d:
    print("bessie")
else:
    print("daisy")