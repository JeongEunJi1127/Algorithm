import sys
from itertools import permutations
input = sys.stdin.readline
n,m = map(int,input().split())
lst = [i for i in range(1,n+1)]
ans = permutations(lst,m)

for i in ans:
    print(*i)