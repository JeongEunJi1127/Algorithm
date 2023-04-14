n = int(input())
maxx = maxy = -10000
minx = miny = 10000

for _ in range(n):
    x,y = map(int,input().split())
    if x > maxx:
        maxx = x
    if x < minx:
        minx = x
    if y > maxy:
        maxy = y
    if y < miny:
        miny = y
        
print((maxx-minx)*(maxy-miny))
    
