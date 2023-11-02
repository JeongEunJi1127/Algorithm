while True:
    parameter = []
    s = input()
    if s == ".":
        break
    for i in s:
        if i == "(" or i == "[":
            parameter.append(i)
        elif i == ")":
            if len(parameter) != 0 and parameter[-1] == "(":
                parameter.pop()
            else:
                parameter.append(i)
                break
        elif i == "]":
            if len(parameter) != 0 and parameter[-1] == "[":
                parameter.pop()
            else:
                parameter.append(i)
                break
    if len(parameter) == 0:
        print("yes")
    else:
        print("no")
        



   
