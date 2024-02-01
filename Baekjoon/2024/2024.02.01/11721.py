n = input()

while n:
    if len(n)< 10:
        print(n)
        break
    print(n[:10])
    n = n[10:]

    