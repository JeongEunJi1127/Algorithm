n = int(input())
lst = []

for _ in range(n):
    lst.append(list(input().split()))

lst.sort(key = lambda a : int(a[0]))

for i in range(len(lst)):
    print(lst[i][0], lst[i][1])