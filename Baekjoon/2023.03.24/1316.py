n = int(input())
cnt = n

for _ in range(n):
    s = input()
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            if s[i+1] in s[:i]: 
                cnt-=1
                break

print(cnt)