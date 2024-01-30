lst = []
length = []
ans = ""

for _ in range(5):
    s = input()
    lst.append(list(s))
    length.append(len(s))

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            ans+=lst[j][i]

print(ans)
