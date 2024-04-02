import pprint 

def solution1(array):
    return array[::-1]

def solution2(array):
    newArr = []
    for i in array:
        newArr.append(i[::-1])
    return newArr

def solution3(array):
    n = len(array)
    m = len(array[0])
    newArr = []
    for i in range(m):
        lst = []
        for j in range(n):
            lst.append(array[j][i])
        newArr.append(lst[::-1])
    return newArr

def solution4(array):
    n = len(array)
    m = len(array[0])
    newArr = []
    for i in range(m):
        lst = []
        for j in range(n):
            lst.append(array[j][m-i-1])
        newArr.append(lst)
    return newArr

def solution5(array):
    n = len(array)
    m = len(array[0])
    newArr = []
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []

    for i in range(n//2):
        lst = []
        for j in range(m//2):
            lst.append(array[i][j])
        arr1.append(lst)
    
    for i in range(n//2):
        lst = []
        for j in range(m//2,m):
            lst.append(array[i][j])
        arr2.append(lst)
        
    for i in range(n//2,n):
        lst = []
        for j in range(m//2,m):
            lst.append(array[i][j])
        arr3.append(lst)
    
    for i in range(n//2,n):
        lst = []
        for j in range(m//2):
            lst.append(array[i][j])
        arr4.append(lst)
    
    for i in range(n//2):
        newArr.append(arr4[i]+arr1[i])
    for i in range(n//2):
        newArr.append(arr3[i]+arr2[i])
    return newArr

def solution6(array):
    n = len(array)
    m = len(array[0])
    newArr = []
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []

    for i in range(n//2):
        lst = []
        for j in range(m//2):
            lst.append(array[i][j])
        arr1.append(lst)
    
    for i in range(n//2):
        lst = []
        for j in range(m//2,m):
            lst.append(array[i][j])
        arr2.append(lst)
        
    for i in range(n//2,n):
        lst = []
        for j in range(m//2,m):
            lst.append(array[i][j])
        arr3.append(lst)
    
    for i in range(n//2,n):
        lst = []
        for j in range(m//2):
            lst.append(array[i][j])
        arr4.append(lst)
    
    for i in range(n//2):
        newArr.append(arr2[i]+arr3[i])
    for i in range(n//2):
        newArr.append(arr1[i]+arr4[i])
    return newArr

n,m,r = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
tlst = list(map(int,input().split()))

for t in tlst:
    if t == 1: array = solution1(array)
    elif t == 2: array = solution2(array)
    elif t == 3: array = solution3(array)
    elif t == 4: array = solution4(array)
    elif t == 5: array = solution5(array)
    elif t == 6: array = solution6(array)

for i in array:
    print(*i)