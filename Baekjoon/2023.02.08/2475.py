a,b,c,d,e = map(int,input().split())

def koi(i,j,k,l,m):
    print((i**2 + j**2 + k**2 + l**2 + m**2) % 10 )

koi(a,b,c,d,e)