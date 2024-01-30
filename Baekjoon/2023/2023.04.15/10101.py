triangle = []
for _ in range(3):
    triangle.append(int(input()))

cnt = 0
sum = 0

for i in triangle:
    if i != 60:
        cnt+=1
    sum += i

if cnt == 0:
    print("Equilateral")
elif sum == 180 and len(set(triangle)) == 3:
    print("Scalene")
elif sum == 180 and len(set(triangle)) == 2:
    print("Isosceles")
elif sum != 180:
    print("Error")