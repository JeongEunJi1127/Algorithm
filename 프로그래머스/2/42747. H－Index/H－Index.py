def solution(citations):
    citations.sort(reverse = True)
    length = len(citations)
    
    for i in range(length):
        if citations[i] < i+1:
            return i       
    return len(citations)