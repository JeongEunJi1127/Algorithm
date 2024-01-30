n = int(input())
k = 2

while True:
    if n == 1:
        break
    elif n % k == 0:
        print(k)
        n = n//k
    else:
        k+=1