import sys
input = sys.stdin.readline
n,m,r = map(int,input().split())
array = []

for _ in range(n):
    array.append(list(map(int,input().split())))

def rotate(array):
    for i in range(min(n,m)//2):
        x,y = i,i
        # 맨 처음 값 저장
        value = array[x][y]

        # 왼쪽
        for j in range(i+1,n-i):
            x = j
            tmp = array[x][y]
            array[x][y] = value
            value = tmp

        # 아래쪽
        for j in range(i+1, m-i): 
            y = j
            tmp = array[x][y]
            array[x][y] = value
            value = tmp

        # 오른쪽
        for j in range(i+1, n-i): 
            x = n - j - 1 
            tmp = array[x][y] 
            array[x][y] = value
            value = tmp

        # 위
        for j in range(i+1, m-i):
            y = m - j - 1
            tmp = array[x][y]
            array[x][y] = value
            value = tmp
    return array

for _ in range(r):
    rotate(array)

for i in array:
    print(*i)