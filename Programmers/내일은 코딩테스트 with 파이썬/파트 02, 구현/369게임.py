def solution(order):
    answer = 0
    lst369 = ["3","6","9"]
    for i in str(order):
        if i in lst369:
            answer+=1
    return answer