def solution(emergency):
    answer = []
    sorted_em = sorted(emergency,reverse = True)
    
    for i in emergency:
        answer.append(sorted_em.index(i) + 1)
    return answer