lst= list(map(int,input().split()))

lst = sorted(lst)

while(lst[2] >= lst[0]+lst[1]):
    lst[2]-=1

print(lst[0]+lst[1]+lst[2])