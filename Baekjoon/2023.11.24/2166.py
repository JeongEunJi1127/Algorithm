n = int(input())
positions = []
ans = 0

for _ in range(n):
    x,y = map(int,input().split())
    positions.append((x,y))
positions.append(positions[0])

for i in range(n):
    ans += positions[i][0] * positions[i+1][1]
    ans -= positions[i][1] * positions[i+1][0]

print(round(abs(ans/2),1))