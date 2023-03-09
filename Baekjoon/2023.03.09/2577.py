a = int(input())
b = int(input())
c = int(input())
ans = {"0": 0,"1" : 0,"2" : 0,"3" : 0,"4" : 0,"5" : 0,"6" : 0,"7" : 0,"8" : 0,"9" : 0}
mul = a * b * c

for i in str(mul):
    ans[i] = ans[i] + 1

for i in ans:
    print(ans[i])


