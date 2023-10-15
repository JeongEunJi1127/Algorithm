n = int(input())
m = 1
cnt = 0

while n >0:
    m = m * n
    n-=1

m = str(m)

for i in m[::-1]:
    if i == "0": 
        cnt+=1
    else:
        print(cnt)
        break