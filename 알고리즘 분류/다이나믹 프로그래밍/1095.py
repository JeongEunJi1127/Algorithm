import sys
input =sys.stdin.readline
# 아이디어 -> 직접 조합 값을 계산하지 않고, 
# 소인수분해하여 소수의 지수 값을 구한 후에, 
# 해당 소수들의 지수 값들을 이용하여 가장 큰 약수를 구한다!

# 지수 구하는 함수 -> 소수 pn이 num에 몇번 나타나는지 구하는 함수이다
def cal(pn,num):
    tmp = num
    # pn의 지수 저장할 변수 d
    d = 0
    # tmp//소수 pn이 양수이면
    while tmp // pn > 0:
        # 나눠주기
        tmp //= pn
        # 지수 +1
        d += tmp
    return d

s, f, m = map(int, input().split())
# 소수
prime = []
# 소수의 지수
cnt = []

# dp 인덱스 설정 - m값 10만
b = 1000000
dp = [True] * (b+1)
# 0,1은 소수가 아님
dp[0] = False
dp[1] = False

# 에라토스테네스의 채 사용 - m의 범위 내에서 소수 찾기
for k in range(2, int(b**0.5) + 1):
    if dp[k] == True:
        # 제곱한 수들 -> 소수가 아님 -> false처리
        for i in range(k*k, b+1, k):
            dp[i] = False

# dp의 범위 내에서
for i in range(b+1):
    # dp[i] = true인 수들, 즉 i가 소수이면
    if dp[i]:
        # 소수 리스트 prime에 i 추가
        prime.append(i)
        # i의 지수 구해서 소수지수 리스트 cnt에 추가 -> cal(i, s+f)는 조합식 "(s+f)!"에서 소수 i의 지수를 구하는 함수. 나머지도 동일
        cnt.append(cal(i,s+f)-cal(i,s)-cal(i,f))

# 다음과 같은 과정이 끝나면 cnt에 소수의 지수들이 남는다

ans = 1
# m부터 1까지 역순으로 돈다
for i in range(m, 0, -1):
    tmp = i
    flag = True
    # 소수 길이만큼 돈다
    for j in range(len(prime)):
        count = 0
        # tmp는 현재 m의 값. 현재 m의 값이 현재 소수 값으로 나누어 떨어지면 tmp갱신 & 지수 값 +=1
        while tmp % prime[j] == 0:
            tmp //= prime[j]
            count += 1
        # count가 해당 소수의 지수보다 크면 => 반복문 종료
        if count > cnt[j]:
            flag = False
            break
    # 반복문을 다 돌았을 때 flag가 true면 현재 탐색중인 i명이 조건 만족 -> for문은 역순으로 도므로 i가 정답이다. 고로 break
    if flag:
        ans = i
        break

print(ans)