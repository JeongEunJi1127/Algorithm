def solution(score):
    answer = []
    lst = []
    for i in score:
        lst.append(sum(i)/2)
    sorted_lst = sorted(lst,reverse = True)
    # print(lst,sorted_lst)
    for i in lst:
        answer.append(sorted_lst.index(i)+1)
    return answer