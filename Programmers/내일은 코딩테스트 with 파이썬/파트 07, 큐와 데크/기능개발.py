from collections import deque
def solution(progresses, speeds):
    answer = []
    days = deque()
    for p,s in zip(progresses, speeds):
        if (100-p) % s == 0:
            day = (100-p) // s
        else:
            day = ((100-p) // s) + 1
        days.append(day)
    
    while days:
        # print(days)
        if len(days) == 1:
            answer.append(1)
            break
        # 첫번째 기능 배포에 걸리는 날
        f1 = days.popleft()
        # 첫번째 기능과 같이 배포될 기능 개수 
        cnt = 1
        for i in days:
            if i <= f1:
                cnt+=1
            else:
                break
        for _ in range(cnt-1):
            days.popleft()
        answer.append(cnt)
    return answer
