# 백준 13711
import sys
import bisect

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

# b를 a의 인덱스로 정렬하는 과정에서 딕셔너리를 써줘야 시간 초과가 안난다.. (index 썻다가 폭망)
dic = {}
for i in range(n):
    dic[a[i]] = i

lst = []
for i in b:
    lst.append(dic[i])

# lst에서 가장 긴 증가하는 부분 수열을 구해주면 답 (LIS), 이진 탐색 써야함
dp = [lst[0]]

for i in range(1,n):
    num = lst[i]
    if dp[-1] < num:
        dp.append(num)
    else:
        # dp 배열에서 num이 삽입될 위치를 반환
        idx = bisect.bisect_left(dp,num)
        dp[idx] = num

print(len(dp))
