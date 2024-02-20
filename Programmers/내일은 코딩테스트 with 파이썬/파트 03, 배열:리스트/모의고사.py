def solution(answers):
    answer = []
    po1 = [1,2,3,4,5] * 2000
    po2 = [2,1,2,3,2,4,2,5] * 1250
    po3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    num, num2, num3 = 0,0,0
    
    for idx,ans in enumerate(answers):
        if ans == po1[idx]:
            num1 += 1
        if ans == po2[idx]:
            num2 += 1
        if ans == po3[idx]:
            num3 += 1
            
    if num1 == max(num1,num2,num3):
        answer.append(1)
    if num2 == max(num1,num2,num3):
        answer.append(2)
    if num3 == max(num1,num2,num3):
        answer.append(3)
    return answer
