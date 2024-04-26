def solution(edges):
    # 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수 출력
    answer = [0,0,0,0]
    
    # 생성된 정점 - 진입차수 0, 진출차수만 있는데 2이상
    # 그래프의 수 - 결국 그래프의 수를 구하는 것이므로 한 그래프 당 어떤 특징을 가진 정점이 잇느ㄴ지 찾는다..?
    # 도넛 모양 그래프 - 모르겟음 ->  (정점에서 나가는 간선의 개수 - 막대모양 도형 개수 - 8자 모양 도형 개수)
    # 막대 모양 그래프 - 진출차수가 0인 정점이 무조건 하나 발생 
    # 8자 모양 그래프 - 진입차수 2 진출차수 2인 정점 조건 하나 발생 - 여기서 생성된 정점에서 들어올 수 있는 진입차수 +1 까지 고려해야함

     # 각 정점들의 진입차수, 진출차수 숫자 계산한 dictionary
    graph = {}
    
    for edge in edges:
        a,b = edge
        try:
            # a의 진출차수 += 1
            graph[a][1] += 1
        except:
            graph[a] = [0,0]
            graph[a][1] += 1
            
        try:
            # b의 진입차수 += 1
            graph[b][0] += 1
        except:
            graph[b] = [0,0]
            graph[b][0] += 1
            
    
    for i in graph.keys():
        enter,out = graph[i]
        
        # 생성된 점
        if (enter == 0 and out >= 2):
            answer[0] = i
        # 막대 모양 그래프
        elif (out == 0 and enter >=0):
            answer[2] += 1
        # 8자 모양 그래프
        elif (enter >= 2 and out == 2):
            answer[3] += 1
            
    # 도넛 모양 그래프 -> (정점에서 나가는 간선의 개수 - 막대모양 도형 개수 - 8자 모양 도형 개수)
    answer[1] = graph[answer[0]][1]-answer[2]-answer[3]
    
    return answer