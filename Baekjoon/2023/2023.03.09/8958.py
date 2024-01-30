n = int(input())
for _ in range(n):
    s = input()
    cnt= 0
    sum = 1
    for i in s:
        if i == "O":
            cnt += sum
            sum += 1
        else:
            sum = 1
    print(cnt)
