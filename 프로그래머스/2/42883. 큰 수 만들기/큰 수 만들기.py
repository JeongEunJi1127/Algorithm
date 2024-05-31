def solution(number, k):
    answer = ''
    lst = []
    
    for num in number:
        if len(lst) == 0:
            lst.append(num)
            continue
        if k > 0:
            while lst[-1] < num:
                k-=1
                lst.pop()
                if k == 0 or len(lst) == 0:
                    break
        lst.append(num)
    answer = ''.join(lst)
    if k>0:
        answer = answer[:-k]
    return answer