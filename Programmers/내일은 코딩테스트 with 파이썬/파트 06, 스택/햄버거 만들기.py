def solution(ingredient):
    answer = 0
    lst = []
    # 1,2,3 순서대로 빵,야채,고기 / 빵,야채,고기,빵 순서로만 포장
    for i in ingredient:  
        lst.append(i)
        
        if len(lst) >= 4:
            checklist = []
            for _ in range(4):
                checklist.append(lst.pop())
            if checklist == [1,3,2,1]:
                answer+=1
            else:
                for i in checklist[::-1]:
                    lst.append(i)
    return answer