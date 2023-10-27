from collections import deque
n = int(input())
deq = deque()

for _ in range(n):
    ipt = input().split()
    if ipt[0] == "push_front":
        deq.appendleft(ipt[1])
    elif ipt[0] == "push_back":
        deq.append(ipt[1])
    elif ipt[0] == "pop_front":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq.popleft())
    elif ipt[0] == "pop_back":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq.pop())
    elif ipt[0] == "size":
        print(len(deq))
    elif ipt[0] == "empty":
        if len(deq) == 0:
            print("1")
        else:
            print("0")
    elif ipt[0] == "front":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[0])
    else:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[-1])