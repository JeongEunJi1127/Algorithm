def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    # 유저별 받은 신고 저장
    dict = {}
    # 유저가 한 신고 저장
    user_report = {}
    
    # 딕셔너리 초기화
    for id in id_list:
        dict[id] = 0
        user_report[id] = []
    
    # dict엔 유저별 받은 신고 수 저장, user_report엔 유저가 신고한 사람 저장
    for i in report:
        re = i.split()
        dict[re[1]] += 1
        user_report[re[0]].append(re[1]) 
        
    # print(dict)
    # print(user_report)
    
    reported_people = []
    for i in dict.items():
        # 신고당한 사람일 경우 저장
        if i[1] >= k:
            reported_people.append(i[0])
            
    for idx,i in enumerate(user_report.items()):
        # print(i)
        for j in i[1]:
            # print(j,reported_people)
            if j and j in reported_people:
                answer[idx] += 1
    
    return answer