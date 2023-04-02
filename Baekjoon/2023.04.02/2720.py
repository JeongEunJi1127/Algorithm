t = int(input())
q = 0
d = 0
n = 0
p = 0
for _ in range(t):
    money = int(input()) 
    q = money // 25
    d = (money % 25) // 10
    n = (money % 25 % 10) // 5
    p = (money % 25 % 10 % 5) 
    print(int(q),int(d),int(n),int(p))


