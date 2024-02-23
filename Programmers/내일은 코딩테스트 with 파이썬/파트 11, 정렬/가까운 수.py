def solution(array, n):
    answer = 0
    num = int(1e9)
    for i in array:
        if abs(i-n) < num:
            answer = i
            num = abs(i-n)
        elif abs(i-n) == num:
            answer = min(i,answer)
    return answer