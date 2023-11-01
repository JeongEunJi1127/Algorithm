from collections import deque
t = int(input())

for _ in range(t):
    n,m = map(int,input().split())   
    lst = deque(input().split())
    ans = deque(i for i in range(n))
    i = 0

    while lst:
        if lst[0] < max(lst):
            lst.append(lst.popleft())
            ans.append(ans.popleft())
        else:
            i+=1
            if ans[0] == m:
                print(i)
                break
            else:
                lst.popleft()
                ans.popleft()

        
    