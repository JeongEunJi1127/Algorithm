def solution(ingredient):
    answer = 0
    hamburger = []
    
    # 1:빵 2:야채 3:고기
    for i in ingredient:
        hamburger.append(i)
        if isBurger(hamburger[-4:]):
            answer += 1
            for _ in range(4):
                hamburger.pop()
    return answer

def isBurger(array):
    if array == [1,2,3,1]:
        return True
    else:
        return False
