def solution(nums):
    answer = 0
    dict = {}
    # 골라야 할 폰켓몬의 개수
    n = len(nums)//2
    for i in nums:
        try:
            dict[i] += 1
        except:
            dict[i] = 1
    
    if len(dict) > n:
        answer = n
    else:
        answer = len(dict)
        
    return answer