from collections import deque
n,k = map(int, input().split())
ans = []
lst = deque([i for i in range(1, n+1)])

while len(lst) != 0:
    for _ in range(k-1):
        lst.append(lst.popleft())
    ans.append(lst.popleft())


print("<",end="")
for i in range(len(ans)-1):
    print(ans[i],end=", ")
print(ans[-1], end="")
print(">")