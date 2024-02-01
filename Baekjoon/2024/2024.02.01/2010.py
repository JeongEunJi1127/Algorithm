import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
for _ in range(n):
    k = int(input())
    cnt+=k

print(cnt-n)
