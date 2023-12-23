import math
a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())
ans1,ans2 = (a1*b2 + a2*b1) , (b1*b2)

n = math.gcd(ans1,ans2) # math 라이브러리의 최대공약수 구하는 함수 사용
ans1,ans2 = ans1//n, ans2//n
print(ans1,ans2)