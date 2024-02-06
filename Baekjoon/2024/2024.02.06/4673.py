all_num = set(i for i in range(1,10001))
lst = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    lst.add(i)
for i in sorted(all_num - lst):
    print(i)