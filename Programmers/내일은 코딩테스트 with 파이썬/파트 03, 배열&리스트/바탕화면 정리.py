def solution(wallpaper):
    answer = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                answer.append((i,j))
    # print(answer)
    minx = answer[0][0]
    maxx = answer[len(answer)-1][0] + 1
    
    answer.sort(key = lambda x:x[1])
    # print(answer)
    miny = answer[0][1]
    maxy = answer[len(answer)-1][1] + 1
    ans = [minx,miny,maxx,maxy]
    return ans