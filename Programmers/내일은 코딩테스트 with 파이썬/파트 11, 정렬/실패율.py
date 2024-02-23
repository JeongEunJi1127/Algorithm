def solution(N, stages):
    answer = []
    # 실패율 저장할 딕셔너리
    dict = {}
    # 유저의 수
    users = len(stages)
    for i in range(1,N+1):
        if users == 0:
            dict[i] = 0
        else:
            dict[i] = stages.count(i)/users
            users -= stages.count(i)
            
    answer = sorted(dict, key = lambda x: dict[x], reverse = True)

    return answer
