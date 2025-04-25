def convert_number_to_binary(s):
    new_s = ''

    while(s != 1):
        if s%2 == 1:
            new_s = '1' + new_s
        else:
            new_s = '0' + new_s
        s //= 2  
    new_s = '1' + new_s

    return new_s

def convert_binary_to_number(s):
    array = list(s)
    binary_number = 0
    n = len(array)
    
    for i in range(n):
        if array[i] == "1":
            binary_number += 2**(n-1-i)
    
    return binary_number

def cnt_one(binary_number):
    cnt = 0
    for i in binary_number:
        if i == "1":
            cnt+=1
    return cnt

def solution(n):
    now_binary_number = convert_number_to_binary(n)
    
    while(True):
        n += 1
        next_binary_number = convert_number_to_binary(n)

        if cnt_one(now_binary_number) == cnt_one(next_binary_number):
            break
    
    return n