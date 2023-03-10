n = int(input())
s = []

for _ in range(n):
    s.append(input())
s = list(set(s))
s.sort()	
s.sort(key=len)

for i in s:
    print(i)
