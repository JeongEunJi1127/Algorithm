x = int(input())
stick = 64
cnt = 0
while True:
    if x == 0:
        break
    if stick > x:
        stick //= 2
    else:
        x -= stick
        cnt += 1
print(cnt)