def solution(survey, choices):
    answer = ''
    score = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for i in range(len(survey)):
        c = choices[i]
        s = survey[i]
        if c == 1 : score[s[0]] += 3
        elif c == 2 : score[s[0]] += 2
        elif c == 3 : score[s[0]] += 1
        elif c == 4 : continue
        elif c == 5 : score[s[1]] += 1
        elif c == 6 : score[s[1]] += 2
        elif c == 7 : score[s[1]] += 3
        
    print(score)
    if score["R"]>= score["T"]:
        answer+= "R"
    else:
        answer+= "T"
    
    if score["C"]>= score["F"]:
        answer+= "C"
    else:
        answer+= "F"
    
    if score["J"]>= score["M"]:
        answer+= "J"
    else:
        answer+= "M"
    
    if score["A"]>= score["N"]:
        answer+= "A"
    else:
        answer+= "N"
        
        
    return answer