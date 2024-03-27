def countMine(mine,x,y):
    cnt = 0
    dir = [[0,-1],[0,1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
    for i in dir:
        dx,dy = x+i[0], y+i[1]
        if dx >= 0 and dy >= 0 and dx < n and dy < n and mine[dx][dy] == "*":
            cnt += 1
    return cnt

n = int(input())
mine = []
user = []

for _ in range(n):
    mine.append(list(input()))
for _ in range(n):
    user.append(list(input()))

mines = []
lose = False
for i in range(n):
    for j in range(n):
        if mine[i][j] == "*":
            mines.append((i,j))
        if user[i][j] == "x":
            if mine[i][j] == "*":
                lose = True
            user[i][j] = str(countMine(mine,i,j))
if lose:
    for i in mines:
        user[i[0]][i[1]] = "*"
for i in user:
    print("".join(i))