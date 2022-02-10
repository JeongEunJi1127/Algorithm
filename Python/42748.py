def solution(array, commands):
    answer = []

    for command in commands:
        i,j,k = command
        strr = array[i-1:j]
        strr.sort()
        answer.append(strr[k-1])

    return answer



