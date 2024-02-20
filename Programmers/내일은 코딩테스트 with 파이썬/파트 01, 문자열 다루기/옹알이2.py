def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for j in can_speak:
            if j*2 not in i:
                i = i.replace(j," ")
        if i.isspace():
            answer += 1
    return answer