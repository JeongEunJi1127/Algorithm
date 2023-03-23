c = int(input())

for _ in range(c):
    lst = list(map(int,input().split()))
    avg = 0
    cnt = 0
    avg = sum(lst[1:])/lst[0]
    for i in lst[1:]:
        if i>avg:
            cnt+=1
    # print(str(round(cnt/lst[0] * 100,3))+"%")
    print("{:.3f}%".format(cnt/lst[0] * 100))