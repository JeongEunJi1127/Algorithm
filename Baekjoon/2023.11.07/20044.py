n = int(input())
stu_power = list(map(int,input().split()))

stu_power.sort()
ans = []

for i in range(n):
    ans.append(stu_power[i] + stu_power[len(stu_power)-1 -i])
print(min(ans))