import pprint

m,n = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(m)]

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[-1]*n for _ in range(m)]

def dfs(x,y):
    # 목표 지점에 도착한 경우, 시작점에서 도착점까지 성공적으로 방문한 1가지 경우가 됨 -> 1 리턴, 지금까지 걸어온 경로에 1을 모두 더해줌
    if x==m-1 and y==n-1:
        return 1

    # 방문하지 않은 지점이면
    if visited[x][y] == -1:
        # 방문 표시
        visited[x][y] = 0
        for i in range(4):
            # 상하좌우 좌표 탐색
            nx,ny = x+dx[i],y+dy[i]
            if nx >= 0 and ny >= 0 and nx < m and ny < n:
                # 더 작은 값이면 이동할 수 있다는 뜻이므로
                if matrix[x][y] > matrix[nx][ny]:
                    # 값 업데이트
                    visited[x][y] += dfs(nx,ny)
    return visited[x][y]

print(dfs(0,0))