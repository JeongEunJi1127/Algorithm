atka, hearta = map(int,input().split())
atkb, heartb = map(int,input().split())

while True:
    hearta -= atkb
    heartb -= atka
    if hearta<=0 and heartb<=0:
        print("DRAW")
        break
    elif hearta <= 0:
        print("PLAYER B")
        break
    elif heartb <= 0:
        print("PLAYER A")
        break