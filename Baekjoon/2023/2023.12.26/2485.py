import math,sys

n = int(sys.stdin.readline())
first = int(sys.stdin.readline())
positions = []
 
for _ in range(n-1):
    position = int(sys.stdin.readline())
    positions.append(position - first)
    first = position
min_distance = math.gcd(*positions)

cnt = 0
for i in positions:
    cnt += i//min_distance -1
print(cnt)