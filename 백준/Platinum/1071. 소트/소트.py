n = int(input())
lst = list(map(int,input().split()))
answer = []

# 각 숫자의 개수를 세는 딕셔너리 생성
countDict = {}
for num in lst:
    if num not in countDict:
        countDict[num] = 1
    else:
        countDict[num] += 1

cnt = 0
while(True):
    if sum(countDict.values()) == 0:
        break
     # cnt 수가 존재 -> 현재 수는 cnt
    if cnt in countDict.keys() and countDict[cnt]>0:
        # 현재 수보다 1 더 큰 수가 존재할 때
        if cnt+1 in countDict.keys() and countDict[cnt+1]>0:
            idx = 1001
            for i in sorted(countDict.keys()):
                if i>cnt+1 and countDict[i]>0:
                    idx = i
                    break

             # 현재 수보다 2이상 더 큰 수가 존재하지 않을 때
            if idx == 1001:
                # +1인 수 하나 출력
                answer.append(cnt+1)
                countDict[cnt+1]-=1
            # 현재 수보다 2이상 더 큰 수가 존재할 때
            else:
                # 현재 수 모두 출력
                for _ in range(countDict[cnt]):
                    answer.append(cnt)
                countDict[cnt]=0
                # +idx인 수 하나 출력
                answer.append(idx)
                countDict[idx]-=1
                cnt += 1
        # 현재 수보다 1 더 큰 수가 존재하지 않을 때
        elif cnt+1 not in countDict.keys() or (cnt+1 in countDict.keys() and countDict[cnt+1]==0):
            # 현재 수 모두 출력
            for _ in range(countDict[cnt]):
                answer.append(cnt)
            countDict[cnt]=0
            cnt += 1
    else:
        cnt+=1

print(*answer)