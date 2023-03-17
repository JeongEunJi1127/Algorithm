n = int(input())
nlst = list(map(int,input().split()))
m = int(input())
mlst = list(map(int,input().split()))

# 이분탐색 이용한 풀이
nlst.sort()

def binary(l,lst,start,end):
    if start > end:
        print(0)
        return
    mid = (start+end)//2
    if l == lst[mid]:
        print(1)
        return
    elif l > lst[mid]:
        start = mid+1
    elif l < lst[mid]:
        end = mid-1
    return binary(l,lst,start,end)

for i in mlst:
    binary(i,nlst,0,n-1)





