n = int(input())
# dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i-1][j])
triangle = []
for _ in range(n):
    triangle.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = triangle[i-1][j-1]
        if j == i:
            up = 0
        else:
            up = triangle[i-1][j]

        triangle[i][j] = triangle[i][j] + max(up,up_left)
print(max(triangle[n-1]))