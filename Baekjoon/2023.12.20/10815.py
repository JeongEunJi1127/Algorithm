import sys
n = int(sys.stdin.readline())
n_lst = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_lst = list(map(int,sys.stdin.readline().split()))

dict = {}
for i in n_lst:
    dict[i] = 0

for i in m_lst:
    if i not in dict:
        print(0,end=" ")
    else:
        print(1,end=" ")