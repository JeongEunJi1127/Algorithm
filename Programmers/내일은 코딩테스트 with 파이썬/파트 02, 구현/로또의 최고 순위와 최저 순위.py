def solution(lottos, win_nums):
    answer = []
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    num = 0
    for i in lottos:
        if i in win_nums:
            num += 1
            
    if num+lottos.count(0) > 6:
        answer.append(rank[6])
    else:
        answer.append(rank[num+lottos.count(0) ])
    answer.append(rank[num])
    return answer