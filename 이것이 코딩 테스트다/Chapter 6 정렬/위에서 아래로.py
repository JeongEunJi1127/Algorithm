n = int(input())
lst = [] 

for _ in range(n):
    s = int(input())
    lst.append(s)
    
lst.sort(reverse=True)
print(*lst)
