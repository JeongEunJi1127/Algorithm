from collections import deque
n = int(input())
deq = deque()

for i in range(n):
    deq.append(i+1)
    
while len(deq) != 1:
    deq.popleft()
    deq.append(deq.popleft())

for i in deq:
    print(i)