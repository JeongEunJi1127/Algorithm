from collections import deque
n = int(input())
deq = deque(enumerate(map(int,input().split())))
ans = []

while deq:
    idx,ballon = deq.popleft()
    ans.append(idx+1)

    if ballon > 0:
        deq.rotate(-(ballon - 1))
    elif ballon < 0:
        deq.rotate(-ballon)

print(' '.join(map(str, ans)))
        