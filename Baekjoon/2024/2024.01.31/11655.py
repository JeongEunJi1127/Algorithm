n = input()
ans = ''

for i in range(len(n)):
    if n[i] == ' ' or ord(n[i]) < ord('A'):
        ans += n[i]
    else:
        if ord(n[i]) + 13 > 122:
            ans += chr(96 + (ord(n[i]) + 13) - 122)
        elif ord(n[i]) + 13 > 90 and ord(n[i]) < 91:
            ans += chr(64 + (ord(n[i]) + 13) - 90)
        else:
            ans += chr(ord(n[i]) + 13)
print(ans)