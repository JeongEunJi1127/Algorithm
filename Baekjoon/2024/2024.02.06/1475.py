n = input()
dp = [0] * (10)
for i in n:
    dp[int(i)] += 1
max_num = 0
sum69 = 0
for idx,i in enumerate(dp):
    if idx == 6 or idx == 9:
        sum69 += i
    else:
        max_num = max(max_num,i)

if max_num >= sum69:
    print(max_num)
else:
    if sum69 % 2 == 0:
        print(sum69//2)
    else:
        print(sum69//2+1)