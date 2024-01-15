import sys
n,k = map(int,sys.stdin.readline().split())
temperature = list(map(int,sys.stdin.readline().split()))
# 첫 번째 연속된 k일 온도의 합을 구해놓는다
sums = sum(temperature[:k])
# 모든 합을 저장해놓을 리스트 lst 선언, 첫번째 온도 합 저장
lst = [sums]

for i in range(len(temperature)-k):
    # 다음 연속된 온도 합 = 바로 이전 온도 합 - 이전 연속된 날짜 중 가장 앞 날짜의 온도 + 다음 순번의 k번째 온도
    sums = sums - temperature[i] + temperature[i+k]
    lst.append(sums)
print(max(lst))
    