n = str(input())
lst = []

for i in n:
    lst.append(int(i))
lst.sort(reverse=True)

for i in lst:
    print(i,end="")