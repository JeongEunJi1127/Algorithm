import sys
from collections import Counter
n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    lst.append(int(sys.stdin.readline()))

print(round(sum(lst)/n)) # 산술평균

lst.sort()
print(lst[n//2]) # 중앙값

# 최빈값
ans = Counter(lst).most_common()
if len(ans) == 1:
    print(ans[0][0]) 
else:
    if ans[0][1] == ans[1][1]:
        print(ans[1][0])
    else:
        print(ans[0][0])


print(max(lst)-min(lst))# 범위

