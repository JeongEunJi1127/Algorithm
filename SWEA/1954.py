T = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0] # 동남서북

for test_case in range(1, T+1):
    n = int(input())
    lst = [[0] * n for _ in range(n)]
    dir = 0 # 방향벡터
    num = 1 # 달팽이 배열에 넣을 숫자
    x,y = 0,0 # 인덱스 x,y
    lst[0][0] = 1 # 첫 시작위치 1

    while True:
        if n==1 :
            break
        if num == n * n:
            break
        if x+dx[dir] < 0 or x+dx[dir] >= n or y+dy[dir] < 0 or y+dy[dir] >= n or lst[x + dx[dir]][y + dy[dir]] != 0:
            dir += 1
            if dir >= 4:
                dir = 0
        x,y = x + dx[dir],y + dy[dir]
        num += 1
        lst[x][y] = num

    print("#"+str(test_case))
    for i in lst:
        print(*i) # []을 언팩하기 위해 사용
