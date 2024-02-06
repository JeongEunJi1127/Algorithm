people = 0
ans = []
for _ in range(4):
    a,b = map(int,input().split())
    people += b
    people -= a
    ans.append(people)
print(max(ans))