def solution(s):
    stack = []
    
    for i in s.split():
        if i == "Z":
            stack.pop()
        else:
            stack.append(int(i))
    answer = sum(stack)
    return answer