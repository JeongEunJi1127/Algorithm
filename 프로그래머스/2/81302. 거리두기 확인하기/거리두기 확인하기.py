from collections import deque

def Bfs(array):
    # 첫 응시자의 위치 구하기
    peoples = deque()
    dx = [-1,1,0,0]  
    dy = [0,0,-1,1]
    
    for i in range(5):
        for j in range(5):
            if array[i][j] == "P":
                queue = deque([(i,j,0)])
                visited = [[False]*5 for _ in range(5)]
                visited[i][j] = True

                while queue:
                    x,y,distance = queue.popleft()
                    
                    if distance > 2:
                        break
                        
                    for dir in range(4):
                        nx,ny = x+dx[dir], y+dy[dir]

                        if nx>=0 and ny>=0 and nx<5 and ny<5 and not visited[nx][ny]:
                            # p는 응시자, 0는 빈 테이블, X는 파티션 
                            if array[nx][ny] == "X":
                                continue
                            elif array[nx][ny] == "P":
                                if distance+1 <= 2:
                                    return 0
                            queue.append((nx,ny,distance+1))
                            visited[nx][ny] = True
    return 1
    

def solution(places):
    answer = []
       
    for place in places:
        answer.append(Bfs(place))

    return answer