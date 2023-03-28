max = 0
x = 0
y = 0

for i in range(9):
    lst = list(map(int,input().split()))
    for j in range(9):
        if max <= lst[j]:
            max = lst[j]
            x = i+1
            y = j+1
print(max)
print(x,y,end=" ")

