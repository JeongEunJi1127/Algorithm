t = int(input())

for _ in range(t):
    h,w,n = map(int,input().split())
    
    floor = (n%h) * 100
    door = (n//h) + 1
    if floor == 0:
        floor = h*100
        door -= 1
    print(floor+door)