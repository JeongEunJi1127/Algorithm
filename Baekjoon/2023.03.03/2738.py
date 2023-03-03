n,m = map(int, input().split())
arr = []
    
for _ in range(n):
    arr.append(list(map(int, input().split())))

for j in range(n):
    lst = list(map(int, input().split()))
    for i in range(m):
        arr[j][i] += lst[i]

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
