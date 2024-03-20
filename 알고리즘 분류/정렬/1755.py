a,b = map(int,input().split())
array = []
dic = {"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine", "0":"zero"}
for i in range(a,b+1):
    string = ""
    for j in str(i):
        string += dic[j]
    array.append((string,i))
array.sort()

cnt = 0
for i in array:
    cnt += 1
    print(i[1],end=" ")
    if cnt == 10:
        cnt = 0
        print( )
