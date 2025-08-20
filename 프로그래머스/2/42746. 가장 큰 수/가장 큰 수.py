def findMax(numbers):
    global answer
    num = '0'
    removenum = 0

    if numbers == []  :
        return

    for number in numbers:
        if int(str(number)[0]) > int(num[0]):
            num = str(number)  # 첫 숫자 가져오기
            removenum = number

        # 앞 글자가 같을때 풀이 참고,,
        elif int(str(number)[0]) == int(num[0]):
            if int((str(number)*3)[1]) > int(str(num*3)[0]):
                num = str(number)
                removenum = number

    answer += num
    numbers.remove(removenum)

    findMax(numbers)

def solution(numbers):
    global answer
    answer = ''

    findMax(numbers)
    return answer