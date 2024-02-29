n = int(input())
m = int(input())
s = input()

p, cnt, ans = 0, 0, 0

while p < (m - 1):
    if s[p:p + 3] == 'IOI': #3칸
        cnt += 1
        p += 2
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        p += 1
        cnt = 0

print(ans)
