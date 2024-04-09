def solution(survey, choices):
    answer = ''
    n = len(survey)
    
    personality = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    
    for i in range(n):
        if choices[i] < 4:
            personality[survey[i][0]] += abs(choices[i]-4)
        elif choices[i] > 4:
            personality[survey[i][1]] += (choices[i]-4)
    
    if personality["R"] >= personality["T"] : answer += "R"
    else: answer += "T"
    
    if personality["C"] >= personality["F"] : answer += "C"
    else: answer += "F"
    
    if personality["J"] >= personality["M"] : answer += "J"
    else: answer += "M"
    
    if personality["A"] >= personality["N"] : answer += "A"
    else: answer += "N"
    
    return answer