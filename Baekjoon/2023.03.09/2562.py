max = 0
ans = []

for _ in range(9):
    ans.append(int(input()))

for i in ans:
    if i>max:
        max = i
print(max)
print(ans.index(max)+1)
