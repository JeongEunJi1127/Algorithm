# array에서 num 숫자 visited 처리 후 빙고 존재하는지 확인하는 함수
def is_bingo(array,num,visited):
    cross1 = [(0,0),(1,1),(2,2),(3,3),(4,4)]
    cross2 = [(0,4),(1,3),(2,2),(3,1),(4,0)]
    cnt = 0
    for i in range(5):
        if num in array[i]:
            # array 에서 num의 위치 기준 x,y
            x,y = i,array[i].index(num)
            visited[x][y] = True
            break

    # 가로 확인
    for i in range(5):
        bingoX = True
        for j in range(5):
            if not visited[i][j]:
                bingoX = False
        if bingoX:
            cnt += 1

    # 세로 확인
    for i in range(5):
        bingoY = True
        for j in range(5):
            if not visited[j][i]:
                bingoY = False
        if bingoY:
            cnt += 1

    # 대각선1 확인
    bingoZ1 = True
    for i in cross1:
        if not visited[i[0]][i[1]]:
            bingoZ1 = False
    if bingoZ1:
        cnt += 1

    # 대각선2 확인
    bingoZ2 = True
    for i in cross2:
        if not visited[i[0]][i[1]]:
            bingoZ2 = False
    if bingoZ2:
        cnt += 1

    return cnt

array = []
mc = []
visited = [[False] * 5 for _ in range(5)]
ans = 0
cnt = 0

for _ in range(5):
    array.append(list(map(int,input().split())))
for _ in range(5):
    mc.append(list(map(int,input().split())))

for i in mc:
    for j in i:
        ans += 1
        num = is_bingo(array,j,visited)
        if num >= 3:
            break
    if num >= 3:
        break
print(ans)

