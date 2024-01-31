x,y = map(int,input().split())
lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekend = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
ans = 0

for i in range(x-1):
    ans = ans + lst[i]
ans = (ans + y) % 7
print(weekend[ans])