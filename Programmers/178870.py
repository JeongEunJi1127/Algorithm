def solution(sequence, k):
    answer = []
    
    n = len(sequence)
    start = 0
    end = 0
    sumNum = sequence[start]
    
    while True:
        if sumNum >= k:
            if sumNum == k:
                answer.append([start,end])
            sumNum -= sequence[start]
            start+=1
            if start >= n:
                break  
        elif sumNum < k:
            end += 1
            if end >= n:
                break
            sumNum += sequence[end]
    
    for i in range(len(answer)):
        answer[i].append(answer[i][1]-answer[i][0])
    answer.sort(key = lambda x: (x[2],x[0],x[1]))
    
    return answer[0][0:2]

