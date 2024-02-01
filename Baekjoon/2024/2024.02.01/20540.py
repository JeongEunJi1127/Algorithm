s = input()
ans = ''
for i in s:
    if i == "I":
        ans += "E"
    elif i == "E":
        ans += "I"
    elif i == "S":
        ans += "N"
    elif i == "N":
        ans += "S"
    elif i == "T":
        ans += "F"
    elif i == "F":
        ans += "T"
    elif i == "J":
        ans += "P"
    elif i == "P":
        ans += "J"
print(ans)
