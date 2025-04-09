# 15:10 ~ 15:1

import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
array = [i for i in range(1,n+1)]

def solution(): 
    permus = list(permutations(array))
    
    for permu in permus:
        print(*permu)

solution()