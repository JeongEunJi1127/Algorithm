import sys
input = sys.stdin.readline
q = int(input())

for _ in range(q):
    a = int(input())
    t = int(bin(a)[2:])
    if t&(-t) == a:
        print(1)
    else:
        print(0)

    