import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    ipt = sys.stdin.readline().split()
    if ipt[0] == "push":
        queue.append(ipt[1])
    elif ipt[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif ipt[0] == "size":
        print(len(queue))
    elif ipt[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif ipt[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif ipt[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)