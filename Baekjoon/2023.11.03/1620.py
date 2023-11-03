import sys
pokeName = {}

n,m = map(int,input().split())
for i in range(n):
    ipt = sys.stdin.readline().strip()
    pokeName[i+1] = ipt
    pokeName[ipt] = i+1

for _ in range(m):
    prb = sys.stdin.readline().strip()
    if prb.isdigit():
        print(pokeName[int(prb)])
    else:
        print(pokeName[prb])