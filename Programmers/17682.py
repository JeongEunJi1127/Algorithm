def solution(scores):
    answer = []
    divide_score = []

    # 세 개의 형태(점수|보너스|[옵션])로 나누기
    if scores[2] == "#" or scores[2] == "*":
        divide_score.append(scores[:3])
        scores = scores[3:]
    elif scores[1] == "0" : # 점수가 10점일 경우
        if scores[3] == "#" or scores[3] == "*":
            divide_score.append(scores[:4])
            scores = scores[4:]
        else:
            divide_score.append(scores[:3])
            scores = scores[3:]
    else:
        divide_score.append(scores[:2])
        scores = scores[2:]
    # 한번 더
    if scores[2] == "#" or scores[2] == "*":
        divide_score.append(scores[:3])
        scores = scores[3:]
        divide_score.append(scores)
    elif scores[1] == "0" : # 점수가 10점일 경우
        if scores[3] == "#" or scores[3] == "*":
            divide_score.append(scores[:4])
            scores = scores[4:]
            divide_score.append(scores)
        else:
            divide_score.append(scores[:3])
            scores = scores[3:]
            divide_score.append(scores)
    else:
        divide_score.append(scores[:2])
        scores = scores[2:]
        divide_score.append(scores)

    # 3개의 점수 계산하기
    for score in divide_score:
        print("현재 계산중인 스코어는:",score)

        now_score = 0
        if "10" in score:
            now_score = 10
        else:
            now_score = int(score[0])

        print("현재 정수 스코어", now_score)

        if "S" in score:
            answer.append(now_score)
        elif "D" in score:
            answer.append(now_score ** 2)
        elif "T" in score:
            answer.append(now_score ** 3)

        print("sdt 계산 후 스코어", answer[-1])

        if "#" in score:
            answer[-1] *= -1 # 맨 뒤에 append
        elif "*" in score:
            answer[-1] *= 2
            if len(answer) != 1:
                answer[-2] *= 2

        print("#,* 계산하면?",answer[-1])
        print( )
        print(sum(answer))
    return sum(answer)


# print(solution("1D*2S#3S"))
# print(solution("1D2S3S#"))
print(solution("2D*2S*10S"))