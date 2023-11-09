n = int(input())
cnt = 0

while n % 5 != 0:
    if n <= 5 and n % 2 != 0:
        cnt = -1
        break
    n -= 2
    cnt+=1
if n == 0 or n % 5 == 0:
    cnt += n// 5
print(cnt)
