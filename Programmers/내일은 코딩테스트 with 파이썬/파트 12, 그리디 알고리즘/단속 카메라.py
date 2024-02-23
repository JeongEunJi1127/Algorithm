def solution(routes):
    answer = 0
    # 진출 시점에 대해 오름차순 정렬 
    routes = sorted(routes,key=lambda x:x[1])
    camera = -30001
    
    for i in routes:
        if i[0] > camera:
            camera = i[1]
            answer += 1
    return answer