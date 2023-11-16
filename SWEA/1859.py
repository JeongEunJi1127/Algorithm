T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    price = list(map(int,input().split()))
    benefit = 0
    max = price[-1]
    for i in price[::-1]:
        if i > max:
            max = i
        else:
            benefit += max - i

    print("#"+str(test_case), benefit)