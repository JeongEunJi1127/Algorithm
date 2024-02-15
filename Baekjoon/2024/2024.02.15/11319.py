vowels =  ["A","E","I","O","U","a","e","i","o","u"]
for _ in range(int(input())):
    s = input()
    co = 0
    vo = 0
    for i in s:
        if i.isalpha():
            if i in vowels:
                vo += 1
            else :
                co += 1
    print(co,vo)