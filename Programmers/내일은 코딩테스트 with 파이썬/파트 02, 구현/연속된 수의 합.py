def solution(num, total):
    answer = []
    # n-1, n, n+1 = 3*n, 즉 total//num이 중앙 수이다
    n = total // num 
    answer.append(n)
    cnt = 1
    for _ in range(num // 2):
        answer.append(n+cnt)
        answer.append(n-cnt)
        cnt += 1
    answer.sort()
    if num % 2 == 0:
        if sum(answer[1:]) == total:
            answer = answer[1:]
        elif sum(answer[:-1]) == total:
            answer = answer[:-1]
        
    return answer