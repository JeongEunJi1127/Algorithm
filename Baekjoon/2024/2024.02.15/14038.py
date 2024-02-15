cnt = 0
for _ in range(6):
    s = input()
    if s == "W":
        cnt += 1

if cnt == 0:
    print(-1)
elif cnt <= 2:
    print(3)
elif cnt <= 4:
    print(2)
else:
    print(1)