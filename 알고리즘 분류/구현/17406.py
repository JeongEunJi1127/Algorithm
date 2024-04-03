from itertools import permutations
import copy
import sys
input = sys.stdin.readline

def countLine(array):
    minSum = int(1e9)
    for i in array:
        minSum = min(minSum,sum(i))
    return minSum

def rotateArray(array,r,c,s):
    x,y,a,b = r-s-1,c-s-1,r+s-1,c+s-1

    for i in range(min((a-x),(b-y))//2):
        nx,ny,mx,my = x+i,y+i,a-i,b-i       
        value = array[nx][ny]

        # 위
        for j in range(ny+1,my+1):
            tmp = array[nx][j]
            array[nx][j] = value
            value = tmp
        
        # 오른쪽
        for j in range(nx+1,mx+1):
            tmp = array[j][my]
            array[j][my] = value
            value = tmp

        # 아래
        for j in range(my-1,ny-1,-1):
            tmp = array[mx][j]
            array[mx][j] = value
            value = tmp
        
        # 왼쪽
        for j in range(mx,nx,-1):
            tmp = array[j-1][ny]
            array[j-1][ny] = value
            value = tmp

    return array

n,m,k = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

krr = []
for _ in range(k):
    r,c,s = map(int,input().split())
    krr.append([r,c,s])

permu = list(permutations(krr,len(krr)))

ans = int(1e9)
for i in permu:
    arr = copy.deepcopy(array)
    for j in i:
        r,c,s = j
        rotateArray(arr,r,c,s)
    ans = min(ans,countLine(arr))

print(ans)