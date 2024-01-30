import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque()
ans = deque(int(sys.stdin.readline()) for i in range(n))
plmi = []
i = 1

while ans:
    if len(deq) == 0:
        deq.append(i)
        plmi.append("+")
        i += 1
    elif ans[0] == deq[-1]:
        deq.pop()
        ans.popleft()
        plmi.append("-")
    else:
        if i <= n:
            deq.append(i)
            plmi.append("+")
            i += 1
        else:
            if ans[0] != deq[-1]:
                plmi.clear()
                plmi.append("NO")
                break

for i in plmi:
    print(i)
