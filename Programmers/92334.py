def solution(id_list, report, k):
    answer = []
    
    # [id가 신고당한수, 신고한 id들]을 value에 넣을 거임
    dic = {}
    for id in id_list:
        dic[id] = [0,[]]

    
    for i in report:
        # a는 신고한 id, b는 신고당한 id
        a,b = i.split()
        if b not in dic[a][1]:
            dic[a][1].append(b)
            dic[b][0] += 1
    
    # dic에서 정지된 아이디 뽑기
    lst = []
    for i in dic.items():
        if i[1][0] >= k:
            lst.append(i[0])
    
    for i in dic.values():
        cnt = 0
        for j in lst:
            if j in i[1]:
                cnt+=1
        answer.append(cnt)
    return answer