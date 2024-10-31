from collections import deque

def bfs(land,visited,i,j,oil):
    cnt = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
            
    queue = deque([[i,j]])
    visited[i][j] = True
    columns = set()
    columns.add(j)
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            
            if nx>=0 and ny>=0 and nx<len(land) and ny<len(land[0]) and not visited[nx][ny] and land[nx][ny] == 1:
                cnt += 1
                visited[nx][ny] = True
                queue.append([nx,ny]) 
                columns.add(ny)
    
    for c in columns:
        oil[c] += cnt

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    visited = [[False]*m for _ in range(n)]
    oil = [0] * m 
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(land,visited,i,j,oil)
                  
    answer = max(oil)
#     for i in range(m):
#         cnt = 0
#         visited_oil = set()
#         for j in range(n):
#             # 석유가 있는 땅이고 아직 계산하지 않은 석유 땅의 idx인 경우
#             if ground[j][i][0] and ground[j][i][1] not in visited_oil:
#                 visited_oil.add(ground[j][i][1])
#                 cnt += ground[j][i][2]              
        
#         answer = max(answer,cnt)
    
    return answer