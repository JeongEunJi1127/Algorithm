def solution(k, tangerine):
    answer = 0
    dict = {}
    
    for i in tangerine:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1   
            
    lst = sorted(dict,key = lambda x: -dict[x])    
    
    for i in lst:
        k -= dict[i]
        answer += 1
        if k <= 0:
            break
        
    return answer