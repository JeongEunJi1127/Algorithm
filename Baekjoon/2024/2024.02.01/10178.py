t = int(input())
for _ in range(t):
    c,v = map(int,input().split())
    a = c//v
    b = c%v
    print("You get", a ,"piece(s) and your dad gets", b ,"piece(s).")