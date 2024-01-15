n = int(input())
store = list(map(int,input().split()))
m = int(input())
customer = list(map(int,input().split()))

store.sort()

def binary_search(list,target,start,end):
    if start > end:
        return False
    mid = (start+end)//2
    if target == list[mid]:
        return True
    elif target > list[mid]:
        return binary_search(list,target,mid+1,end)     
    else:
        return binary_search(list,target,start,mid-1) 

for i in customer:
    if binary_search(store,i,0,n-1):
        print("yes", end=" ")
    else:
        print("no", end=" ")