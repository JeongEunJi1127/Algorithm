from itertools import permutations
n = int(input())
lst = [i for i in range(1,n+1)]
perm = list(permutations(lst,2))
print(len(perm))