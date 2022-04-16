def dfs(numbers,target,cnt,ans):
    global answer
    if (cnt == len(numbers)):
        if(ans == target):
            answer+=1
        return

    for d in [-1,1]:
        dfs(numbers, target, cnt+1, ans + d * numbers[cnt])

def solution(numbers, target):
    global answer
    answer = 0

    dfs(numbers,target,0,0)

    return answer

print(solution([1,1,1,1,1], 3))