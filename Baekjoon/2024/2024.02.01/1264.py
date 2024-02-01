mo = ["a","e","i","o","u"]
while True:
    s = input()
    cnt = 0
    if s == "#":
        break

    for i in s.lower():
        if i in mo:
            cnt += 1
    print(cnt)
