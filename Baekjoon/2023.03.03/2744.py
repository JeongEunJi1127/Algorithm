n = input()
ans = ''

for i in n:
    if i.isupper():
        ans += i.lower()
    else:
        ans += i.upper()

print(ans)