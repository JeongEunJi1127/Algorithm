n = int(input())
new_num = str(n)
s = str(n)
cnt = 0

while True:
    if int(s) < 10:
        new_num = new_num[-1] + s[-1]
    else:
        new_num = new_num[-1] + str(int(s[0]) + int(s[1]))[-1]
    cnt += 1
    if int(new_num) == n:
        print(cnt)
        break 
    s = new_num
    