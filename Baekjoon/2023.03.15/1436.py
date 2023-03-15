n = int(input())
cnt = 0
ord = 0
#666이 들어가는 수의 순서
while(True):
    if '666' in str(cnt):
        ord += 1
    if ord == n:
        print(cnt)
        break
    cnt+=1
