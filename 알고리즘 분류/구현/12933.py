str = list(input())
duck = "quack"
cnt = 0
visited = [False] * len(str)

if len(str) % 5 != 0:
    print(-1)
    exit()

def countDuck(start):
    global cnt
    idx = 0
    is_right = True
    for i in range(start, len(str)):
        if str[i] == duck[idx] and visited[i] == False:
            visited[i] = True
            if duck[idx] == 'k':
                if is_right:
                    cnt += 1
                    is_right = False
                idx = 0 
            else:
                idx += 1

for i in range(len(str)):
    countDuck(i)

if cnt == 0 or not all(visited):
    print(-1)
else:
    print(cnt)