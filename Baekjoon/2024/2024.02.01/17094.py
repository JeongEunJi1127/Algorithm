n = int(input())
s = input()
cnt2 = 0
cnte = 0
for i in s:
    if i == "2":
        cnt2 += 1
    else:
        cnte += 1
if cnt2 > cnte:
    print("2")
elif cnt2 < cnte:
    print("e")
else:
    print("yee")