n = int(input())
money = 1000 - n
ans = 0

while money != 0:
    if money >= 500:
        money -= 500
    elif money < 500 and money >= 100:
        money -= 100
    elif money < 100 and money >= 50:
        money -= 50
    elif money < 50 and money >= 10:
        money -= 10
    elif money < 10 and money >= 5:
        money -= 5
    elif money < 5 and money >= 1:
        money -= 1
    
    ans += 1
print(ans)