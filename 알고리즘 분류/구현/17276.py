from collections import deque
import pprint
def rotate45(array):
    # X의 주 대각선을 ((1,1), (2,2), …, (n, n)) 가운데 열 ((n+1)/2 번째 열)로 옮긴다.
    value = deque()
    for i in range(n):
        value.append(array[i][n//2])
        array[i][n//2] = array[i][i]

    # X의 가운데 열을 X의 부 대각선으로 ((n, 1), (n-1, 2), …, (1, n)) 옮긴다. 
    for i in range(n):
        value.append(array[i][n-i-1])
        array[i][n-i-1] = value.popleft()

    # X의 부 대각선을 X의 가운데 행 ((n+1)/2번째 행)으로 옮긴다.
    for i in range(n):
        value.append(array[n//2][n-i-1])
        array[n//2][n-i-1] = value.popleft()

    # X의 가운데 행을 X의 주 대각선으로 옮긴다.
    for i in range(n):
        value.append(array[n-i-1][n-i-1])
        array[n-i-1][n-i-1] = value.popleft()

    return array

t = int(input())
for _ in range(t):
    # n은 홀수
    n,d = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(n)]
    d //= 45
    if d<0:
        d+=8

    for _ in range(d):
        array = rotate45(array)

    for i in array:
        print(*i)