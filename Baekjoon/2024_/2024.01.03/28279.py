import sys
from collections import deque
n = int(sys.stdin.readline())
deq = deque()

for _ in range(n):
    ipt = sys.stdin.readline().split()
    if ipt[0] == "1":
        deq.appendleft(ipt[1])
    elif ipt[0] == "2":
        deq.append(ipt[1])
    elif ipt[0] == "3":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif ipt[0] == "4":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif ipt[0] == "5":
        print(len(deq))
    elif ipt[0] == "6":
        if deq:
            print(0)
        else:
            print(1)
    elif ipt[0] == "7":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif ipt[0] == "8":
        if deq:
            print(deq[-1])
        else:
            print(-1)