from collections import Counter

def solution(participants, completions):
    answer = ''

    # 내가 작성한 코드 - 효율성 테스트 실패
    # for completion in completions:
    #     participants.remove(completion)
    #answer = "".join(participants)

    # counter() 는 리스트 원소들의 개수가 알고 싶을 때 사용 가능하다.
    # answer = Counter(participants)-Counter(completions)
    # answer = list(answer.keys())[0] # 이렇게 key값만 추출 가능하다
    #

    part = dict()

    for participant in participants:
        if participant in part:
            part[participant] += 1
        else:
            part[participant] = 1

    for completion in completions:
        if completion in part:
            part[completion] -= 1
            if part[completion] ==0:
                del(part[completion])

    answer = list(part.keys())[0]
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))