s = input()
cnt = 0
ans = {}
val = ''

for i in s:
    if i.upper() in ans.keys():
        ans[i.upper()] = ans[i.upper()] + 1
    else:
        ans[i.upper()] = 1

max = max(ans.values())

for key,value in ans.items():
    if value == max:
        cnt+=1
        val = key
    
if cnt > 1:
    print("?")
else:
    print(val)
    
    