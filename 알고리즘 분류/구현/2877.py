k = int(input())
# 창영이는 4와 7로 이루어진 수를 좋아한다.
# 1 ≤ K ≤ 10^9

binary = bin(k+1)[3:]

ans = ''
for i in str(binary):
    if i=="0":
        ans += "4"
    elif i == "1":
        ans += "7"
print(ans)