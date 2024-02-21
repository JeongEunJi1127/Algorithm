from itertools import permutations
def solution(spell, dic):
    answer = 2
    lst = []
    
    for i in list(permutations(spell,len(spell))):
        n = ''
        for j in i:
            n += j
        lst.append(n)
    for i in dic:
        if i in lst:
            answer = 1

    return answer