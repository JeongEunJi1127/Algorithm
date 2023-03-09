ans = {}

for _ in range(10):
    i = int(input())
    if i%42 in ans.items():
        ans[i%42] = ans[i%42] + 1
    else:
        ans[i%42] = 1

print(len(ans))