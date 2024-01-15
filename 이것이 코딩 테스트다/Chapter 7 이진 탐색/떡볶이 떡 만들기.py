n, m = map(int,input().split())
rice_cake = list(map(int,input().split()))

start = 0
end = max(rice_cake)
result = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in rice_cake:
        if i > mid:
            cnt += (i-mid)
    if cnt < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)