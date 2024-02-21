def solution(array):
    dict = {}
    for i in array:
        try:
            dict[i] += 1
        except:
            dict[i] = 1
    print(dict.items())

    max_num = max(dict.items(),key = lambda x:x[1])[1]
    cnt = 0
    for i in dict.items():
        if i[1] == max_num:
            cnt+=1
    if cnt > 1:
        answer = -1
    else:
        answer = max_num = max(dict.items(),key = lambda x:x[1])[0]
    
    return answer