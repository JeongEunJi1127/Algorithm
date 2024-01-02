def is_sosu(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num ** 0.5)+1):	
    	if num % i == 0:		
            return False
    return True	
lst = list(range(2,246912))
sosu = []
for i in lst:
    if is_sosu(i):
        sosu.append(i)

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for i in sosu:
        if n < i <= 2*n:
            cnt+=1
        
    print(cnt)

