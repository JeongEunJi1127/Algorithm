n = int(input())
lst = list(map(int,input().split()))
ans = 0
lst.sort()

if len(lst) % 2 == 0:
    ans = lst[0] * lst[-1]
else:
    ans = lst[len(lst)//2] ** 2

print(ans)