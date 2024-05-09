from collections import deque
def solution(s):
    answer = True
    
    q = deque(s[0])
    
    for i in s[1:]:
        if len(q) == 0:
            q.append(i)
        else:
            x = q.popleft()
            if x == ")":
                answer = False
                break
            elif x == "(" and i == "(":
                q.append(x)
                q.append(i)
    if q:
        answer = False
    return answer