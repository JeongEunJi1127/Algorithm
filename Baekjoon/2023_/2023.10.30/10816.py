import sys
from collections import Counter
n = int(sys.stdin.readline())
nlst = list(sys.stdin.readline().split())
m = int(sys.stdin.readline())
mlst = list(sys.stdin.readline().split())

nlst = Counter(nlst)
for i in mlst:
    if i in nlst:
        print(nlst.get(i), end=" ")
    else:
        print("0",end=" ")

