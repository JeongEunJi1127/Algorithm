n,m = map(int,input().split())
result = 0
graph = []

for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    # x,y 범위 벗어나면 False
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 아직 방문하지 않은 노드라면
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1
        # 상하좌우 노드 재귀 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False # 방문한 노드면 바로 False 리턴

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result += 1

print(result)