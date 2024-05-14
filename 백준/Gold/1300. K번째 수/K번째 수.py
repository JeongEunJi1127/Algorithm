import sys
input = sys.stdin.readline

def countNum(idx, n):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(idx // i, n)
    return cnt

def binarySearch(n, k):
    left = 1
    right = k

    while left <= right:
        mid = (left + right) // 2
        if countNum(mid, n) < k:
            left = mid + 1
        else:
            right = mid - 1
    return left

n = int(input())
k = int(input())

answer = binarySearch(n, k)
print(answer)
