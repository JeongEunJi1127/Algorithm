# 이진 탐색, 파라메트릭 서치를 사용하여 풀었다.
import sys
k,n = map(int,sys.stdin.readline().split())
lst = []
for _ in range(k):
    lst.append(int(sys.stdin.readline()))
start = 1
end = max(lst)
result = 0

while start <= end:
    cnt = 0
    mid = (start+end)//2
    for i in lst:
        cnt += i//mid

    if cnt < n:
        end = mid -1
    else:
        result = mid
        start = mid + 1
print(result)

