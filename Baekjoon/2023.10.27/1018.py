n,m = map(int,input().split())
ipt = []
prev = ''
ans = []

for _ in range(n):
    ipt.append(input())

def chessBoard(x,y):
    new_list = []
    for i in range(8):
        new_list.append(ipt[x+i][y:y+8])
    return new_list

for i in range(0,n-7):
    for j in range(0,m-7):
        cnt = 0
        for l in range(8):
            if l == 0:
                prev = chessBoard(i,j)[l][0]
            else:
                if prev == 'B':
                    prev = 'W'
                else:
                    prev = 'B'
            for k in range(8):          
                if chessBoard(i,j)[l][k] != prev:
                    cnt+=1
                if prev == 'W':
                    prev = 'B'
                else:
                    prev = 'W'            
        ans.append(cnt)
        cnt = 0
        for l in range(8):
            if l == 0:
                if chessBoard(i,j)[l][0] == 'B':
                    prev = 'W'
                else:
                    prev = 'B'
            else:
                if prev == 'B':
                    prev = 'W'
                else:
                    prev = 'B'
            for k in range(8):          
                if chessBoard(i,j)[l][k] != prev:
                    cnt+=1
                if prev == 'W':
                    prev = 'B'
                else:
                    prev = 'W'            
        ans.append(cnt)
print(min(ans))


