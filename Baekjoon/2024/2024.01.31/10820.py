while True:
    try:
        small = 0
        big = 0
        number = 0
        blank = 0

        s = input()
        for i in s:
            if i.isdigit():
                number += 1
            elif i.isalpha():
                if i.isupper():
                    big += 1
                elif i.islower():
                    small += 1
            elif i.isspace():
                blank += 1
        print(small,big,number,blank,end = " ")
    except EOFError:
        break