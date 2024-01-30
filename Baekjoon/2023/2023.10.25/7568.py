n = int(input())
lst = []
ord = [1] * n

for i in range(n):
    x,y = map(int, input().split())
    lst.append((x,y))

for i in range(n):
    for j in range(n):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            ord[i] += 1 
           

for i in ord:
    print(i, end= " ")

