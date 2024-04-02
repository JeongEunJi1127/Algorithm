from collections import deque
s = deque(input())
tmp = deque()
is_bool = False
ans = []

def toStr(queue):
    str = ''
    for i in queue:
        str += i
    queue.clear()
    return str

for i in s:
    if i == " ":
        tmp.append(i)
        if is_bool == False:
            ans.append(toStr(tmp))         

    elif i == "<":
        is_bool = True
        tmp.append(i)

    elif i == ">":
        is_bool = False
        tmp.append(i)
        ans.append(toStr(tmp))

    # 괄호 안의 문자 일 경우
    elif is_bool:
        tmp.append(i)
    else:
        tmp.appendleft(i)

if len(tmp) != 0:  
    ans.append(toStr(tmp))

for i in ans:
    print(i,end="")