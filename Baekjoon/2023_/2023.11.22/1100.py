line = 0
cnt = 0

for _ in range(8):
    lst = list(input().split())
    if line % 2 == 0: # 흰 칸으로 시작
        for idx,i in enumerate(lst[0]):
            if idx % 2 == 0 and i == "F":
                cnt += 1
    else:
        for idx,i in enumerate(lst[0]):
            if idx % 2 == 1 and i == "F":
                cnt += 1
    line += 1

print(cnt)