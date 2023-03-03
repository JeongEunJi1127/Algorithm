alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = input()
ans = [-1] * 26

for i in alphabet:
    print(s.find(i),end=' ')

