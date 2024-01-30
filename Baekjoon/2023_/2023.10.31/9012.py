n = int(input())

for _ in range(n):
    ipt = list(input())
    stack = []
    isVPS = True

    for i in ipt:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                print("NO")
                isVPS = False
                break
            else:
                stack.pop()
    if len(stack) == 0 and isVPS:
        print("YES")
    elif len(stack) !=0 and isVPS:
        print("NO")
   
