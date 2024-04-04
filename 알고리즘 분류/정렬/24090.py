import sys
sys.setrecursionlimit(int(1e4)) 
input = sys.stdin.readline

def partition(array,start,end):
    global cnt
    pivot = array[end]
    i = start-1
    for j in range(start,end): 
        if array[j] <= pivot: 
            i +=1
            array[i], array[j] = array[j], array[i]
            cnt += 1
            if cnt == k:
                print(array[i],array[j])

    if i+1 != end:
        array[i+1], array[end] = array[end], array[i+1]
        cnt += 1
        if cnt == k:
            print(array[i+1],array[end])
    return i+1

def quickSort(array,start,end):
    if start >= end:
        return
    q = partition(array,start,end)
    quickSort(array,start,q-1)
    quickSort(array,q+1,end)


n,k = map(int,input().split())
array = list(map(int,input().split()))
cnt = 0

quickSort(array,0,n-1)

if cnt < k:
    print(-1)
