def solution(my_string, num1, num2):
    answer = ''
    word1 = my_string[num1]
    word2 = my_string[num2]
    
    for i in range(len(my_string)):
        if i == num1:
            answer += word2
        elif i == num2:
            answer += word1
        else:
            answer += my_string[i]
    return answer

# 더 좋은 풀이
def solution(my_string, num1, num2):
    answer = ''
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return answer.join(my_string)