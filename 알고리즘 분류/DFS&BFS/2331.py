def get(n):
    num = 0
    for i in str(n):
        num += int(i)** p
    return num

a,p = map(int,input().split())
lst = [a]

while True:
    num = get(a)
    if num in lst:
        s = num
        break
    lst.append(num)
    a = num
print(len(lst[:lst.index(s)]))