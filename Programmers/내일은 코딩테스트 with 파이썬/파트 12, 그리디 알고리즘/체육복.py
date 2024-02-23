def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    
    for i in reserve[:]:
        # 도난당한 학생 중 여벌 체육복이 있는 경우 제외
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
                
    answer = n - len(lost)
    return answer