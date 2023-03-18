# 계수 정렬
import sys

n = int(sys.stdin.readline())
lst = [0] * 10001

for _ in range(n):
    a = int(sys.stdin.readline())
    lst[a] += 1

for i in range(len(lst)):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)



