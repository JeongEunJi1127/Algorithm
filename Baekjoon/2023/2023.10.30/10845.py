import sys

n = int(sys.stdin.readline())
queue = []

for _ in range(n):
    ipt = sys.stdin.readline().split()

    if ipt[0] == "push":
        queue.append(ipt[1])
    elif ipt[0] == "pop":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.pop(0))
    elif ipt[0] == "size":
        print(len(queue))   
    elif ipt[0] == "empty":
        if len(queue) == 0:
            print("1")
        else:
            print("0")
    elif ipt[0] == "front":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])
    elif ipt[0] == "back":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[-1])
