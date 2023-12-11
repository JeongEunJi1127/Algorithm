lst = []
ans = 0
for _ in range(5):
    lst.append(int(input()))

lst.sort()
ans = lst[2]

print(sum(lst)//len(lst))
print(ans)