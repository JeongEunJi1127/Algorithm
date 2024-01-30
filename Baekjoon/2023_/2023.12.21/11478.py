s = input()
lst = set()
for i in range(len(s)+1):
    for j in range(i,len(s)+1):
        lst.add(s[i:j])
print(len(lst)-1)