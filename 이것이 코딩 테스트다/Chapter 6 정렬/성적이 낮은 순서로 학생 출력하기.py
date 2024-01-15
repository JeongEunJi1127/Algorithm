n = int(input())
dict = {}

for _ in range(n):
    name, grade = map(str,input().split())
    dict[name] = grade

dict = sorted(dict,key = lambda data:data[1],reverse = True)
print(*dict)