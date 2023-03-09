lst = list(map(int,input().split()))
acd = 1
dsd = 8

for i in lst:
    if i == 1:
        if acd == 1:
            acd += 1
        elif dsd != 1:
            dsd -= 1
    elif i == 8:
        if dsd == 8:
            dsd -= 1
        elif acd != 8:
            acd += 1
    else:
        if i != acd and i != dsd:
            print("mixed")
            acd=0
            dsd = 0
            break 
        else:
            acd += 1
            dsd -= 1

if acd == 8:
    print("ascending")
if dsd == 1:
    print("descending")

        