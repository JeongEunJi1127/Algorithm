def sosu(i):
    if i == 1:
        return False
    for j in range(2,i+1):
        if j == i:
            continue
        if i % j == 0:
            return False
            break
    return True


m = int(input())
n = int(input())
add = 0
min = n
cnt = 0


for i in range(m,n+1):
    if sosu(i):
        if i < min:
            min = i
        add += i
        cnt += 1
    

if cnt == 0 :
    print(-1)
else:
    print(add)
    print(min)