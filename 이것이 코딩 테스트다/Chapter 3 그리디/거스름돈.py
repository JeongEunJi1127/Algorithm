n = 1260 # 거슬러 줘야할 돈
coin_types = [500,100,50,10] # 거스름돈 종류
cnt = 0 # 동전의 최소 개수

for coin in coin_types:
    cnt += n // coin # coin으로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin 

print(cnt)