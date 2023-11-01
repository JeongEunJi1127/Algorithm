import sys
from collections import deque
def roundNum(i):
    flo = i - int(i) 
    if flo>=0.5:
        return int(i)+1
    else:
        return int(i)

n = int(sys.stdin.readline())
k = roundNum(n * 0.15)
lst = deque()

for _ in range(n):
    opinion = int(sys.stdin.readline())
    lst.append(opinion)
lst = deque(sorted(lst))
for _ in range(k):
    lst.popleft()
    lst.pop()
if n == 0:
    print("0")
else:
    print(roundNum(sum(lst)/len(lst)))