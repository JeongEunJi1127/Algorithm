import sys
n = int(sys.stdin.readline())

def fibonacci(num):
    if num == 1:
        return 1
    x0 = 0
    x1 = 1
    fibo = 0
    while num>1:
        fibo = x0+x1
        x0 = x1
        x1 = fibo
        num-=1
    return fibo

print(fibonacci(n))
