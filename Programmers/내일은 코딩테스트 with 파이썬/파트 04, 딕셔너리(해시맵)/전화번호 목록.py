def solution(phone_book):
    answer = True
    dict = {}
    for nums in phone_book:
        dict[nums] = 1
    
    for nums in phone_book:
        arr = ''
        for num in nums:
            arr += num     
            if arr in dict and arr != nums:
                answer = False      
    return answer