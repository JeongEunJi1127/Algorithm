def solution(strings, n):
    answer = strings

    answer.sort()
    answer.sort(key=lambda x: x[n])

    return answer