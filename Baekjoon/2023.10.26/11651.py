n = int(input())
lst = []

for _ in range(n):
    x,y = map(int, input().split())
    lst.append((x,y))
lst.sort(key = lambda x :(x[1],x[0]))

for i in lst:
    print(i[0], i[1], end= " ")
    print( )