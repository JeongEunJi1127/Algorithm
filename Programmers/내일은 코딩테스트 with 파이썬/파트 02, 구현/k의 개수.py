def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        num = str(num)
        for n in num:
            if n == str(k):
                answer+=1
    return answer