s = input()

cnt0 = 0
cnt1 = 0

prev = s[0]
if prev == "1":
    cnt1 += 1
else:
    cnt0 += 1

for i in s:
    if i != prev:
        prev = i
        if i == "0":
            cnt0+=1
        else:
            cnt1+=1
print(min(cnt0,cnt1))