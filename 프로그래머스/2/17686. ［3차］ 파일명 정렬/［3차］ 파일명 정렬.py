
from collections import defaultdict

def solution(files):
    answer = []
    dic = defaultdict(list)
    
    for file in files:
        Head = ''
        Number = ''
        Tail = ''
        
        length = len(file)
        i = 0

        # Head 추출
        while i < length and not file[i].isdigit():
            Head += file[i]
            i += 1

        # Number 추출
        while i < length and file[i].isdigit():
            Number += file[i]
            i += 1

        # Tail은 나머지
        Tail = file[i:]
        #print("헤드",Head,"숫자",Number,"꼬리",Tail)

        dic[Head.lower()].append((Number,Tail,Head))
        sorted_header = sorted(dic.keys())

        for key in sorted_header:
            dic[key].sort(key=lambda x:(int(x[0])))
    dic = dict(sorted(dic.items()))
    #print(dic)
    for key in dic.keys():
        for value in dic[key]:
            Number,Tail,Head = value
            answer.append(Head+Number+Tail)
    print(answer)                         
    return answer
