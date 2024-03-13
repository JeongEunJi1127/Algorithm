# bfs
from collections import deque
import pprint

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find_SafeIdx(matrix):
    for idx,i in enumerate(matrix):
        # 안전지역이 하나라도 있으면 즉시 리턴
        if 0 in i:
            return [(idx,i.index(0))]
    return (101,101)

def bfs(matrix):
    # 방문 리스트
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    while True:
        # water 에서 안전지대의 idx 뽑기
        queue = deque(find_SafeIdx(matrix))
        if queue[0] == 101:
            break

        while queue:
            x,y = queue.popleft()
            matrix[x][y] = 2
            visited[x][y] = 1
            for i in range(4):
                nx,ny= x+dx[i],y+dy[i]
                if nx >= 0 and ny >=0 and nx <n and ny<n:
                    if matrix[nx][ny] == 0 and visited[nx][ny] == 0:
                        matrix[nx][ny] = 2
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
        cnt += 1
    return cnt

ans = 0
for h in range(100):
    # h 높이 이하 잠긴 배열, 0은 안전지역, 1은 잠긴 지역
    water = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            # h 높이 이하의 잠기는 지역 1로 표시
            if matrix[i][j] <= h:
                water[i][j] = 1
    ans = max(ans,bfs(water))
print(ans)