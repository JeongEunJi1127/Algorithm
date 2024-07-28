def solution(elements):
    answer = 0
    n = len(elements)
    # 중복체크 - set 사용
    sumValues = set()  
    newElements = elements * 2

    for i in range(1, n+1):
        for j in range(n):
            val = sum(newElements[j:j+i])
            sumValues.add(val)
    answer = len(sumValues)
    return answer
