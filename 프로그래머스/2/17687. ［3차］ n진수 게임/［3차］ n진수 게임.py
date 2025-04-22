def convert(n,base):
    digits = "0123456789ABCDEF"
    result = ""
    if n == 0:
        return "0"
    
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result
    

def solution(n, t, m, p):
    answer = ''
    
    value = ''
    number = 0
    while len(value) < t * m:
        value += convert(number, n)
        number += 1
    
    for i in range(p-1,t * m,m):
        answer += value[i]
        
    return answer