import sys
sys.setrecursionlimit(int(1e4)) 
input = sys.stdin.readline

def partition(array,start,end):
    global lst
    pivot = array[end]
    i = start-1
    for j in range(start,end): 
        if array[j] <= pivot: 
            i +=1
            array[i], array[j] = array[j], array[i]
            lst.append([array[i], array[j]])

    if i+1 != end:
        array[i+1], array[end] = array[end], array[i+1]
        lst.append([array[i+1], array[end]])

    return i+1

def quickSort(array,start,end):
    if start >= end:
        return
    q = partition(array,start,end)
    quickSort(array,start, q-1)
    quickSort(array,q+1, end)


n,k = map(int,input().split())
array = list(map(int,input().split()))
lst = []

quickSort(array,0,n-1)

if len(lst) < k:
    print(-1)
else:
    s = lst[k-1]
    s.sort()
    print(*s)
