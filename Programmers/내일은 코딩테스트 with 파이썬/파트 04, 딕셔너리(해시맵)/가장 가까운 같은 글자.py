def solution(s):
    answer = {}
    ans = []
    for idx,i in enumerate(s):
        try:
            ans.append(idx - answer[i])
            answer[i] += (idx-answer[i])
        except:
            answer[i] = idx
            ans.append(-1)
    return ans