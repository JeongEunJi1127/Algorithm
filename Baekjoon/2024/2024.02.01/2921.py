n = int(input())
cnt = 0

for i in range(n+1):
    for j in range(i,n+1):
        cnt += (i+j)
print(cnt)