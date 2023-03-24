n,m = map(int,input().split())
b = []

for i in range(n):
    b.append(i+1)

for _ in range(m):
    i,j,k = map(int,input().split())
    b = b[0:i-1]+b[k-1:j]+b[i-1:k-1]+b[j:]

for i in b:
    print(i,end=" ")