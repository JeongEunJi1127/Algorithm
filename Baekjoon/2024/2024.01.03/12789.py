n = int(input())
students = list(map(int,input().split()))
order = [] # 한명씩 줄서있는 공간
m = 1

for student in students:
    if student != m:
        order.append(student)
    else:
        m+=1
        while order and order[-1] == m:
            order.pop()
            m+=1

while True:
    if len(order) == 0:
        print("Nice")
        break
    if order.pop() != m:
        print("Sad")
        break
    else:
        m+=1

