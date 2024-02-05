from itertools import combinations
lst = []
for _ in range(9):
    lst.append(int(input()))
comb = combinations(lst,7)
ans = []
for i in comb:
    if sum(i) == 100:
        ans = sorted(i)
for i in ans:
    print(i)