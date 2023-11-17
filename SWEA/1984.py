t = int(input())

for test_case in range(1,t+1):
    lst = list(map(int,input().split()))

    lst.sort()
    lst.remove(lst[0])
    lst.remove(lst[-1])
    print("#"+str(test_case),round(sum(lst)/len(lst)))