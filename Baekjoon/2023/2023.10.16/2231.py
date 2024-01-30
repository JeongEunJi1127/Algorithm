def sumN(a):
    b = str(a)
    sum = 0
    for i in b:
        sum += int(i)
    return a + sum


n = int(input())
ans = 1

while ans < n:
    if sumN(ans) == n:
        break
    else:
        ans += 1

if ans == n:
    print("0")
else:
    print(ans)



