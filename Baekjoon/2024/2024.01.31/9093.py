t = int(input())
for _ in range(t):
    s = list(input().split())
    for i in s:
        print(i[::-1],end = " ")
