n = int(input())
ans = ''
for i in range(n):
    s = input()
    if i == 0:
        ans = s
    else:
        ss = ''
        for j in range(len(s)):
            if ans[j] == s[j]:
                ss += ans[j]
            else:
                ss += '?'
        ans = ss

print(ans)