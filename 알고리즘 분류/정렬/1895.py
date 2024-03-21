r,c = map(int,input().split())
matrix = []
for i in range(r):
    matrix.append(list(map(int,input().split())))
t = int(input())
ans = []
for i in range(r-2):
    for j in range(c-2):
        lst = []
        for a in range(3):
            for b in range(3):
                lst.append(matrix[i+a][j+b])
        lst.sort()
        ans.append(lst[4])
cnt = 0
for i in ans:
    if i >= t:
        cnt+=1
print(cnt)