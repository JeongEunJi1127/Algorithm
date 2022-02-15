def solution(new_id):
    answer = ''
    character = '~!@#$%^&*()=+[{]}:?,<>/'

    # [1] .lower() : 대문자를 소문자로 바꾸어 주는 메소드
    # [2] string.join() 메소드는 괄호 안의 요소를 string과 결합하여 새 문자열을 반환해줌
    new_id = "".join(x for x in new_id.lower() if x not in character)

    # [3] 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    for el in range(len(new_id)):
        if el == 0:
            answer += new_id[el]
        elif (new_id[el] == new_id[el-1]) and (new_id[el] == "."):
            answer
        else:
            answer += new_id[el]

    # [4] index 메서드를 통해 마침표 위치 알아내서 제거
    # strip 메소드를 몰랐을 때의 내 답 => 여기서 런타임 에러 발생
    # if answer.index(".") == 0 :
    #     answer = answer[1:]
    # if (answer != "") and (answer[::-1].index(".") == 0) :
    #     answer = answer[:len(answer)-1]

    # strip 메소드 사용하면!
    answer = answer.strip(".")

    # [5] 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if answer == "" :
        answer= "a"

    # [6] 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(answer) >= 16 :
        answer = answer[:15]
        if answer[14] == ".":
            answer = answer[:14]

    # [7] 길이가 2자 이하라면, 마지막 문자를 answer의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(answer) <= 2:
        answer += answer[-1]

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm."))
print(solution("=.="))
print(solution("abcdefghijklmn.p"))