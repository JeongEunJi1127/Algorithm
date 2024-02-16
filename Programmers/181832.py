def solution(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    # 동남서북
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y = 0,0
    matrix[x][y] = 1
    num = 2
    k = 0
    for i in range(n*n*2):
        nx,ny = x + dx[k],y+dy[k]
        if nx < 0 or nx >= n or ny <0 or ny >= n or matrix[nx][ny] != 0:
            k += 1
            if k == 4:
                k-=4
            continue
        elif matrix[nx][ny] == 0:
            matrix[nx][ny] = num
            num += 1
            x,y = nx,ny
    return matrix