def solution(s):
    answer = ""
    strr = ""
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in s:
        index = 0
        if i.isdigit():  # 만약 i가 정수라면
            answer += i
        else:
            strr += i
            for j in num:
                index += 1
                if strr == j:
                    answer += str(index-1)
                    strr = ""

    answer = int(answer)
    return answer



