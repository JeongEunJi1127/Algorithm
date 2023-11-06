n,m,k = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

first = data[-1]
second = data[-2]
ans = 0

# 1. M의 크기가 작을 때
while True:
    for i in range(k): # k번 first 더하기
        if m==0:
            break
        ans += first
        m-=1
    # 한 번 second 더하기
    if m==0:
        break
    ans+= second
    m-=1

print(ans)

# 2. M의 크기가 클 때
cnt = int(m/(k+1)) * k
cnt += m % (k+1)

ans += cnt * first
ans += (m-cnt) * second

print(ans)
