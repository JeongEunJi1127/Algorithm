year = int(input())
date = int(input())
if year > 2:
    print("After")
elif year < 2:
    print("Before")
else:
    if date == 18:
        print("Special")
    elif date > 18:
        print("After")
    else:
        print("Before")