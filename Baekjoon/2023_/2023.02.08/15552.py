# 시간초과
# t = int(input())
# for _ in range(t):
#     a,b = map(int, input().split())
#     print(a+b)

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)

