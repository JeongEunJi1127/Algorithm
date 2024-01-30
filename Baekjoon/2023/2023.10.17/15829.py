l = int(input())
n = input()
answer = 0

for i in range(len(n)):
    num = ord(n[i])-96
    answer += num * (31 ** i)

print(answer%1234567891)
