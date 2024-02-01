for _ in range(3):
    lst = list(map(int,input().split()))
    if sum(lst) == 4:
        print("E")
    elif sum(lst) == 3:
        print("A") 
    elif sum(lst) == 2:
        print("B") 
    elif sum(lst) == 1:
        print("C") 
    else:
        print("D")