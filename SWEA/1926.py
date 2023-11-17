n = int(input())
ans = []

for num in range(1, n + 1):
    num = str(num)
    cnt = 0
    clap = ''

    for i in str(num):
        if i == "3" or i == "6" or i == "9":
            cnt += 1
    if cnt == 0:
        ans.append(num)
    else:
        for _ in range(cnt):
            clap += "-"
        ans.append(clap)

for i in ans:
    print(i,end=" ")


