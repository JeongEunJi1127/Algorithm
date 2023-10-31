n = int(input())
cnt = 0

if n>=5:
    while n > 0:
        if n < 3:
            cnt = -1
            break
        if n % 5 == 0:
            cnt += n//5
            break
        else:
            n -= 3
            cnt += 1
else:
    if n % 3 == 0:
        cnt += n//3
    else:
        cnt = -1
print(cnt)