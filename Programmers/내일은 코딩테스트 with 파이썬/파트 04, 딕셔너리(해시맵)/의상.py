def solution(clothes):
    answer = 0
    dict = {}

    for cloth in clothes:
        try:
            dict[cloth[1]].append(cloth[0])
        except:
            dict[cloth[1]] = [cloth[0]]
    print(dict)

    n = 1
    for i in dict:
        n *= len(dict[i]) + 1
    answer += n
    return answer-1