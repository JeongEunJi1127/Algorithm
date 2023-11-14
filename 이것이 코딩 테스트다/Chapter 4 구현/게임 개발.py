n,m = map(int,input().split()) # 행m, 열n
a,b,d = map(int,input().split()) # 좌표 (a,b), 바라보는 방향 d
checked_map = [[0] * m for _ in range(n)] # 방문한 위치 표시해 놓을 map
game_map = []

dx = [-1,0,1,0]
dy = [0,1,0,-1] # 북동남서

for _ in range(n):
    game_map.append(list(map(int,input().split())))

def turn_left(): # 왼쪽으로 회전시키는 함수
    global d
    d -= 1
    if d == -1:
        d = 3

checked_map[a][b] = 1 # 첫 시작 위치
cnt = 1 # 캐릭터가 방문한 칸의 수
turn_time = 0 # 캐릭터가 이동하지 못한 횟수

while True:
    turn_left()
    na = a + dx[d]
    nb = b + dy[d]
    # 왼쪽에 가보지 않은 칸이 존재하고 그 칸이 육지라면
    if checked_map[na][nb] == 0 and game_map[na][nb] == 0:
        checked_map[na][nb] = 1
        a = na
        b = nb
        cnt += 1
        turn_time = 0
        continue
    # 왼쪽에 가보지 않은 칸이 없다면
    else:
        turn_time += 1

    # 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 경우
    if turn_time == 4:
        na = a - dx[d]
        nb = b - dy[d]
        # 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우
        if game_map[na][nb] == 1:
            break
        # 뒤쪽 방향으로 한 칸 뒤로 가기
        else:
            a = na
            b = nb

        turn_time = 0

print(cnt)
