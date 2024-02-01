Soongsil,Korea,Hanyang = map(int,input().split())
if Soongsil + Korea + Hanyang >= 100:
    print("OK")
else:
    if min(Soongsil,Korea,Hanyang) == Soongsil:
        print("Soongsil")
    elif min(Soongsil,Korea,Hanyang) == Korea:
        print("Korea")
    else:
        print("Hanyang")