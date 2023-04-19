def MenOfPassion(A, n) :
    sum = 0
    for i in range(1, n - 1):
        for j in range(i + 1,n):
            sum += A[i] * A[j] # 코드1
    return sum

n = int(input())
print(int(n*(n-1)/2))
print(2)