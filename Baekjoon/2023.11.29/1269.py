a,b = map(int,input().split())

set_a = set(input().split())
set_b = set(input().split())
cnt = 0

for i in set_a:
    if i not in set_b:
        cnt+=1
for i in set_b:
    if i not in set_a:
        cnt+=1
print(cnt)