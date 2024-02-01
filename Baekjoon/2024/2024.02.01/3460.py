t = int(input())
for _ in range(t):
    n = int(input())
    a = bin(n)[2:]
    for i in range(len(a)):
        if a[-i-1] == '1':
            print(i, end = " ")