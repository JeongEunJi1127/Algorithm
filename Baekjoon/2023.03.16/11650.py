n = int(input())
lst = []

for _ in range(n):
    x, y = map(int,input().split())
    lst.append((x,y))

lst.sort()
for i in lst:
    print(i[0],i[1])
            