def MenOfPassion(A, n) :
    sum = 0
    for i in range(1,n):
        for j in range(1,n):
            sum += A[i] * A[j] # 코드1
    return sum


n = int(input())

print(n**2)
print(2)