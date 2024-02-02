def solution(today, terms, privacies):
    answer = []
    nowy,nowm,nowd = today.split(".")
    # 약관 저장
    period = {}

    for term in terms:
        x,y = term.split()
        period[x] = y
    
    for i, privacy in enumerate(privacies):
        day, per = privacy.split()
        py,pm,pd = day.split(".")
        
        # 기준날 날짜로 표현
        if pm == 1:
            num = int(pd)
        else:
            num = int(pm) * 28 + int(pd)
        # 약관에 따라 더해야 할 날의 수
        plus = int(period[per]) * 28
        # 보관 가능한 날
        until = num + plus - 1

        untild = until%28
        untilm = until//28
        untily = int(py)
        while True:
            if untilm <= 12:
                break
            untily += 1
            untilm -= 12
        if untild == 0:
            untilm -=1 
            untild = 28
            
        print()
        print(untily,untilm,untild)
        print(nowy,nowm,nowd)
        print( )
        if untily < int(nowy):
            answer.append(i+1)
        elif untily == int(nowy):
            if untilm < int(nowm):
                answer.append(i+1)
            elif untilm == int(nowm):
                if untild < int(nowd):
                    answer.append(i+1)
    return answer