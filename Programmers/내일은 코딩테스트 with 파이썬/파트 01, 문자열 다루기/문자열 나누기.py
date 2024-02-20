def solution(s):
    answer = []
    fir = s[0]
    num = fir
    cnt1 = 1
    cnt2 = 0
    
    for i in range(1,len(s)-1):
        num += s[i]
        if s[i] == fir:
            cnt1 += 1
        else:
            cnt2 += 1
            
        if cnt1 == cnt2:
            answer.append(num)
            fir = s[i+1]
            num = ""
    num += s[-1]
    answer.append(num)
    return len(answer)