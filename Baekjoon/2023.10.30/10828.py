import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    ipt = sys.stdin.readline().split()

    if ipt[0] == "push":
        stack.append(ipt[1])
    elif ipt[0] == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif ipt[0] == "size":
        print(len(stack))   
    elif ipt[0] == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif ipt[0] == "top":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])

