from itertools import permutations

def check_sosu(number):
    global answer
    #print("check 소수",number)
    if number < 2:
        return
        
    for i in range(2,number):
        if number % i == 0:
            return
        
    #print("살아남은 소수", number)
    answer.add(number)
    
def solution(numbers):
    global answer
    answer = set()
    numbers = list(numbers)

    n = len(numbers)
    
    for i in range(1,n+1):
        permus = list(permutations(numbers,i))
        for permu in permus:
            cur_num = int("".join(permu))
            check_sosu(cur_num)
          
    return len(answer)