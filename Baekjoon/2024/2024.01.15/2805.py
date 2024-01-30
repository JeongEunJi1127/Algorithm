import sys
n,m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
start = 0
end = max(lst)
result = 0

while start <= end:
    cnt = 0
    mid = (start+end)//2
    for i in lst:
        if i > mid:
            cnt += (i-mid)
    if cnt < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1
print(result)

