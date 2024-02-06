n = int(input())
mid = 1
side = n-1
for i in range(n):
    print(" "*side + "*"*mid)
    mid += 2
    side -= 1
