def solution(my_string):
    answer = 0
    string = "".join(i if i.isdigit() else " " for i in my_string)
    string = string.split()
    for i in string:
        answer += int(i)
    return answer