import sys

n = sys.stdin.readline()
lst = list(map(int, sys.stdin.readline().split()))
set_lst = sorted(list(set(lst)))

dic = {set_lst[i] : i for i in range(len(set_lst))}
for i in lst:
    print(dic[i], end = ' ')