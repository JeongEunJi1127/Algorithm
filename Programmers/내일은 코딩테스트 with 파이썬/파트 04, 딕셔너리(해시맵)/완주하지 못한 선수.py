def solution(participant, completion):
    dict = {}
    sum = 0
    for i in participant:
        dict[hash(i)] = i
        sum += hash(i)
        
    for j in completion:
        sum -= hash(j)
        
    return dict[sum]
