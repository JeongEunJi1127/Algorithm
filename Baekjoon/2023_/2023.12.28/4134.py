n = int(input())

def is_sosu(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num ** 0.5)+1):	
    	if num % i == 0:		
            return False
    return True	

for _ in range(n):
    k = int(input())
    while is_sosu(k) == False:
        k+=1
    print(k)
