from itertools import product
def solution(word):
    answer = 0
    alphabet = ['A', 'E', 'I', 'O', 'U']
    array = []
    
    for i in range(1,6):
        for j in product(alphabet,repeat = i):
            array.append(''.join(j))
    
    array.sort()

    return array.index(word)+1