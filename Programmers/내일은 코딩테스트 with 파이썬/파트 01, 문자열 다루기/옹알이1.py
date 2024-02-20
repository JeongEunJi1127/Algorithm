from itertools import permutations
def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    can_speak_ = ["aya", "ye", "woo", "ma"]
    for i in range(2,5):
        lst = list(permutations(can_speak,i))
        word = ''
        for j in lst:
            for k in j:
                word += k
            can_speak_.append(word)
            word = ''
    for i in babbling:
        if i in can_speak_:
            answer += 1
    return answer