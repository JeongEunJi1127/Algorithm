n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s = []

for i in range(n):
    s.append(min(a)*max(b))
    a.remove(min(a))
    b.remove(max(b))
print(sum(s))
