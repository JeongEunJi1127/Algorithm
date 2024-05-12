import sys
input = sys.stdin.readline
min,max = map(int,input().split())
answer = 0

# 최대 1,000,000
notSquareNums = [True] * (max-min+1)

# 약 1,000,000번의 for문 - 에라토스 테네스
for i in range(2,int(max**0.5)+1):
    # 기준 제곱수
    squareNum = i**2
    while squareNum <= max:
        idx = int(min/squareNum)*squareNum
        for j in range(idx,max+1,squareNum):
            if j<min:
                continue
            if notSquareNums[j-min]:
                notSquareNums[j-min] = False
        # i의 배수 처리
        squareNum *= i

for i in notSquareNums:
    if i:
        answer+=1
print(answer)
