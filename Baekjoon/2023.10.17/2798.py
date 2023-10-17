from itertools import combinations
n,m = map(int,input().split())
lst = list(map(int,input().split()))
combi = list(combinations(lst,3))
max = 0

for i in combi:
    cnt = 0
    for j in i:
        cnt += j
    if cnt > max :
        if cnt <= m:
            max = cnt
        

print(max)