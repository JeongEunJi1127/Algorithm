def odds(num):
    cnt = 0
    for i in num:
        if int(i)%2 == 1:
            cnt+=1
    return cnt

def solution(num,odd):
    if len(num) == 1:
        lst.append(odd)
        return
    elif len(num) == 2:
        solution(str(int(num[0]) + int(num[1])),odd+odds(str(int(num[0]) + int(num[1]))))
    else:
        for i in range(1,len(num)):
            for j in range(i+1,len(num)):
                part1 = num[0:i]
                part2 = num[i:j]
                part3 = num[j:]
                solution(str(int(part1) + int(part2) + int(part3)),odd+odds(str(int(part1) + int(part2) + int(part3))))
n = input()
lst = []
solution(n,odds(n))  
print(min(lst), max(lst))
