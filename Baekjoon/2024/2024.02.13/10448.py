# 45번째 삼각수 == 1035, 1000 넘으므로 여기까지
tri = [i * (i + 1) // 2 for i in range(1, 46)] 
ans = [0] * 1001

for i in tri:
    for j in tri:
        for k in tri:
            num = i + j + k
            if num <= 1000:
                ans[num] = 1 

t = int(input())
for _ in range(t):
    print(ans[int(input())])