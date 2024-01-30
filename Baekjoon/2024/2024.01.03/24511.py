from collections import deque
import sys
# 배열의 개수
n = int(sys.stdin.readline())
# 배열의 형식 - 0은 큐, 1은 스택
a = list(map(int,sys.stdin.readline().split()))
# 배열에 들어갈 숫자 - 자료구조 
b = list(map(int,sys.stdin.readline().split()))
# 삽입할 수열의 길이
m = int(sys.stdin.readline())
# 수열 c
c = list(map(int,sys.stdin.readline().split()))

queuestack = deque()

for i in range(n):
    # 스택 고려 x
    if a[i] == 0: # 큐인 데이터만 다룸
        queuestack.appendleft(b[i])
# 큐인 데이터의 popleft 값이 출력된 후 (큐이기 때문에) 입력되는 c의 수열 값이 출력된다
if len(queuestack) == 0: # 배열의 형식이 모두 스택일 경우 입력되는 수열 c만 출력하면 됨.
    print(*c)
else:
    for i in range(m):
        queuestack.append(c[i])
        print(queuestack.popleft(),end=" ")







