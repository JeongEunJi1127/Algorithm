a, b = input().split()
ra = ''
rb = ''

for i in reversed(a):
    ra+=i
for i in reversed(b):
    rb+=i

print(max(int(ra),int(rb)))