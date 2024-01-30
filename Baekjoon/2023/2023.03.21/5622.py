s = input()
dic = {2:"ABC",3:"DEF",4:"GHI",5:"JKL",6:"MNO",7:"PQRS",8:"TUV",9:"WXYZ"}
ans = 0

for i in s:
    for j in range(2,10):
        for k in dic[j]:
            if i == k:
                ans += j+1

print(ans)

