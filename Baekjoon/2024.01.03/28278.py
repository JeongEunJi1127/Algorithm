import sys
n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    x = sys.stdin.readline().split()
    if int(x[0]) == 1:
        stack.append(int(x[1]))
    elif int(x[0]) == 2:
        if len(stack) != 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif int(x[0]) == 3:
        print(len(stack))
    elif int(x[0])== 4:
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    elif int(x[0]) == 5:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)