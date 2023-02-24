sdt = []
for i in range(30):
    sdt.append(i+1) 


for _ in range(28):
    num = input()
    if int(num) in sdt:
        sdt.remove(int(num))

print(sdt[0])
print(sdt[1])

