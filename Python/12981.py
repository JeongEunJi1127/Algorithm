def solution(n, words):
    answer = []
    lst = words[0][0]
    # idx = 0
    wrds = []

    for idx,word in enumerate(words):
        # idx += 1  # 현재 단어가 몇번째 단어인지
        wrds.append(word)
        if word[0] != lst or len(set(wrds)) != len(wrds):
            answer.append((idx)%n+1)
            answer.append((idx)//n+1)
            return answer
        elif word[0] == lst: # 끝말잇기 규칙 성립
            lst = word[-1]
            # if idx == len(words):
            #     answer = [0,0]

    return [0,0]
