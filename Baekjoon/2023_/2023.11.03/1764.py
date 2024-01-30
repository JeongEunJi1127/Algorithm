import sys
n,m = map(int,sys.stdin.readline().split())
nohear = set()
noseen = set()

for _ in range(n): 
    nohear.add(sys.stdin.readline().strip())
for _ in range(m):
    noseen.add(sys.stdin.readline().strip())

ans = list(nohear & noseen)
ans.sort()
print(len(ans))
for i in ans:
    print(i)