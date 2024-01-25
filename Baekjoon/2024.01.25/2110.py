import sys
input = sys.stdin.readline
n,c = map(int,input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

# 최소 거리 1로 설정
start = 1
# houses는 정렬된 배열이므로 최대 거리 end =  houses[-1] - houses[0]
end = houses[-1] - houses[0]

def binary_search(list,start,end):
    ans = 0
    while start <= end:
        mid = (start+end) // 2
        # 설치할 수 있는 공유기의 수
        cnt = 1
        prev = houses[0]
    
        for i in range(len(houses)):
            if houses[i] >= mid + prev:
                cnt += 1
                prev = houses[i]
        if cnt >= c:
            start = mid+1
            ans = mid
        else:
            end = mid-1
    return ans
    
print(binary_search(houses,start,end))
                
