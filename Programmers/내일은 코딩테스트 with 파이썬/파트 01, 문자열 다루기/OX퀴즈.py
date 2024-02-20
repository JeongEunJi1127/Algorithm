def solution(quiz):
    answer = []
    for q in quiz:
        q = q.split()
        ans = int(q[0])
        for i in range(1,len(q),2):
            if q[i] == "+":
                ans += int(q[i+1])
            elif q[i] == "-":
                ans -= int(q[i+1])
        if ans == int(q[-1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer