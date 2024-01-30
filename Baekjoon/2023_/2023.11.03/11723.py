import sys
m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    ipt = list(sys.stdin.readline().split())
    if ipt[0] == "add":
        S.add(int(ipt[1]))
        
    elif ipt[0] == "remove":
        if int(ipt[1]) in S:
            S.remove(int(ipt[1]))
        
    elif ipt[0] == "check":
        if int(ipt[1]) in S:
            print("1")
        else:
            print("0")
        
    elif ipt[0] == "toggle":
        if int(ipt[1]) in S:
            S.remove(int(ipt[1]))
        else:
            S.add(int(ipt[1]))

    elif ipt[0] == "all":
        S = {i for i in range(1,21)}
        
    elif ipt[0] == "empty":
        S.clear()
        
