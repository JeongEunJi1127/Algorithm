import sys
sys.setrecursionlimit(int(1e5)) 
input = sys.stdin.readline

def quickSort(array,start,end):
    global is_same
    
    if start >= end:
        return 
    
    pivot = start
    left = start +1
    right = end
    
    # 초기 배열도 정렬 과정에서 발생 가능한 경우로 생각하기
    if array == arrayB:
        is_same = True

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

        if array == arrayB:
            is_same = True
    
    quickSort(array,start,right-1)
    quickSort(array,right+1,end)


n = int(input())
arrayA = list(map(int,input().split()))
arrayB = list(map(int,input().split()))

is_same = False
quickSort(arrayA,0,n-1)

if is_same:
    print(1)
else:
    print(0)
