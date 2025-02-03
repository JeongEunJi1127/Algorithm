# 보고 품
n, r, c = map(int, input().split())

ans = 0

while n != 0:

	n -= 1

	# 제2사분면
	if r < 2 ** n and c < 2 ** n:
		ans += ( 2 ** n ) * ( 2 ** n ) * 0

	# 제1사분면
	elif r < 2 ** n and c >= 2 ** n: 
		ans += ( 2 ** n ) * ( 2 ** n ) * 1
		c -= ( 2 ** n )
        
	# 제3사분면    
	elif r >= 2 ** n and c < 2 ** n: 
		ans += ( 2 ** n ) * ( 2 ** n ) * 2
		r -= ( 2 ** n )
        
	# 제4사분면    
	else:
		ans += ( 2 ** n ) * ( 2 ** n ) * 3
		r -= ( 2 ** n )
		c -= ( 2 ** n )
    
print(ans)
