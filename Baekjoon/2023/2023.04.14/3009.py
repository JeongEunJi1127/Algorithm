x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

if x1 == x2:
   ansx = x3
else:
   if x1 == x3:
      ansx = x2
   else:
      ansx = x1

if y1 == y2:
   ansy = y3
else:
   if y1 == y3:
      ansy = y2
   else:
      ansy = y1
   


print(ansx, ansy)
